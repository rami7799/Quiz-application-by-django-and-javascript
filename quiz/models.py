from django.db import models


DIFF_CHOICES =(
    ('easy','easy'),
    ('medium','medium'),
    ('hard','hard'),
)


class Quiz(models.Model):
    name = models.CharField(max_length=150)
    topic = models.CharField(max_length=200)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="Duration of the quiz in minute")
    required_score_to_pass = models.IntegerField(help_text="required score to %")
    difficulty = models.CharField(max_length=10 , choices=DIFF_CHOICES)

    def __str__(self):
        return f"{self.name}-{self.topic}"

    class Meta:
        verbose_name_plural = "Quizes"