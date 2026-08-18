from django.db import models
from subject.models import Subject
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Quiz(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    duration = models.IntegerField(default=30)
    total_marks = models.IntegerField(default=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)
    question = models.TextField()
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=200)

    def __str__(self):
        return self.question

class Result(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)
    score = models.IntegerField()
    total = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return f"{self.student.username}-{self.quiz.title}"
