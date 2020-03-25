from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=250)
    pub_date = models.DateTimeField('date publication')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=500)
    vote = models.IntegerField(default=0)