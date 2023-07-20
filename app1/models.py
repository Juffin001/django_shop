from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class box(models.Model):
    box_title = models.CharField(max_length=400)
    box_image = models.ImageField(upload_to="app1/static/images")
    box_adress = models.CharField(max_length=200)
    box_pub_date = models.DateTimeField("date published")
    box_price = models.CharField(max_length=50)
    def __str__(self):
        return self.box_title