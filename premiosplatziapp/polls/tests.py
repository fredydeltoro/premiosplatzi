from asyncio import futures
import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question

class QuestionModelTests(TestCase):

  def test_was_published_recently_with_future_questions(self):
    """was_published_recently returns False for questions whose pub_date is in the future"""
    time = timezone.now() + datetime.timedelta(days=30)
    future_question = Question(question_text="¿Quien es el mejore cd de platzi?", pub_date=time)
    self.assertIs(future_question.was_publish_recently(), False)
  
  def test_was_published_recently_with_present_questions(self):
    """was_published_recently returns True for questions whose pub_date is in the present"""
    present_question = Question(question_text="¿Quien es el mejore cd de platzi?", pub_date=timezone.now())
    self.assertIs(present_question.was_publish_recently(), True)
  
  def test_was_published_recently_with_past_questions(self):
    """was_published_recently returns False for questions whose pub_date is in the past"""
    time = timezone.now() - datetime.timedelta(days=30)
    past_question = Question(question_text="¿Quien es el mejore cd de platzi?", pub_date=time)
    self.assertIs(past_question.was_publish_recently(), False)