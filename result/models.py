from django.db import models
from django.contrib.auth.models import User
from quiz.models import Quiz


class Result(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , null=True)
    quiz = models.ForeignKey(Quiz , on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.user.username + self.quiz.name