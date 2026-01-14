import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

#model representing the questions logic, utilizing build in django model subclasses.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("Date Published")

    def __str__(self):
        return self.question_text #method to make question visable as string in command line

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1) #method to give questions published within the last day



#model representing voting choice logic, creating foreign key to link question to choice. also includes voting/text logic
class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE) #Names like question, choice_text and votes will be used as columns names in DB
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text #Same as question class, makes question visable in cmd
