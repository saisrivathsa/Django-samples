from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model) :
    question_text = models.TextField(max_length=100)
    pub_date = models.DateTimeField()

    def __str__(self) :
        return self.question_text
    def was_published_recently(self):
        return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice (models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.TextField(max_length=50)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text



