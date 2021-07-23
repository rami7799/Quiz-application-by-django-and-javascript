from django.db import models
from quiz.models import Quiz


class Question(models.Model):
    text = models.CharField(max_length=150)
    quiz = models.ForeignKey(Quiz , on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)



class Answer(models.Model):
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"question: {self.question.text}, answer: {self.text}, correct: {self.correct}"