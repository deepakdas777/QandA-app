from __future__ import unicode_literals
from django.db import models


class Question(models.Model):
    question_num = models.CharField(max_length = 2)
    question = models.CharField(max_length = 200)
    choice1 = models.CharField(max_length = 200)
    choice2 = models.CharField(max_length = 200)
    choice3 = models.CharField(max_length = 200)
    choice4 = models.CharField(max_length = 200)
    choice5 = models.CharField(max_length = 200)
    answer = models.CharField(max_length = 200)

    def __str__(self):
        return self.question
