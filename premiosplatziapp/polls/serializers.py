from dataclasses import fields
from statistics import mode
from django.contrib.auth.models import User, Group
from .models import Question, Choice
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="polls:user-detail")
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="polls:question-detail")
    class Meta:
        model = Question
        fields = '__all__'

class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="polls:choice-detail")
    class Meta:
        model = Choice
        fields = ['url', 'choice_text', 'votes']