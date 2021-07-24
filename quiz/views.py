from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import Quiz
import random
from question.models import Question , Answer
from result.models import Result


def home(request):
    quizes = Quiz.objects.all()
    context = {
        "quiz" : quizes
    }
    return render(request , "home.html" , context)


def quiz_view(request , pk):
    quiz = Quiz.objects.get(pk=pk)
    # if Result.objects.filter(user=request.user , quiz_id=quiz.id).exists():
    #     return render(request , "before_done.html")

    return render(request , "quiz.html" , {"obj" : quiz})


def quiz_data_view(request , pk):
    quiz = Quiz.objects.get(pk=pk)
    # if Result.objects.filter(user=request.user , quiz_id=quiz.id).exists():
    #     return JsonResponse({"error" : "invalid"})

    question = []
    for q in quiz.question_set.all():
        answers = []
        for answer in q.answer_set.all():
            answers.append(answer.text)
        question.append({str(q.text) : answers})

    random.shuffle(question)

    return JsonResponse({"data" : question , "time" : quiz.time})


def quiz_save_data(request , pk):
    if request.is_ajax():
        data = request.POST
        data_ = dict(data.lists())
        data_.pop("csrfmiddlewaretoken")
        questions = []

        for key in data_.keys():
            # print("key: " , key)
            question = Question.objects.get(text=key)
            questions.append(question)
        print(questions)

        user = request.user
        quiz = Quiz.objects.get(pk=pk)
        quiz.done = True
        quiz.save()

        score = 0
        multiplier = 100 / quiz.number_of_questions
        results = []
        correct_answer = None

        for q in questions:
            a_selected = request.POST.get(str(q))
            print("selected: " , a_selected)  

            if a_selected != "":
                question_answers = Answer.objects.filter(question=q)
                for a in question_answers:
                    if a_selected == a.text:
                        if a.correct:
                            score += 1
                            correct_answer = a.text
                    else:
                        if a.correct:
                            correct_answer = a.text
                results.append({str(q) : {"correct_answer" : correct_answer , "answered" : a_selected}})
            else:
                results.append({str(q) : "Not Answered"})

        score_ = score 
        # Result.objects.create(user=user , quiz_id=quiz.id , score=score_)

    return redirect("/")

        # if score_ >= quiz.required_score_to_pass:
        #     return redirect("/")
        # else:
        #     return redirect("/")