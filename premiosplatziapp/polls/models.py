from datetime import datetime
from pyexpat import model
from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model):
  question_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField("date publish")

  def __str__(self):
    return self.question_text

  def was_publish_recently(self):
    return self.pub_date >= timezone.now() - datetime.timedelta(days=1) and self.pub_date <= timezone.now() + datetime.timedelta(days=1)

class Choice(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)

  def __str__(self):
    return self.choice_text
  