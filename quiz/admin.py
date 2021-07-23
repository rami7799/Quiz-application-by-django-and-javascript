from django.contrib import admin
from .models import Quiz
from question.models import Question

class QuestionAdmin(admin.TabularInline):
    model = Question

class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionAdmin]

admin.site.register(Quiz , QuizAdmin)