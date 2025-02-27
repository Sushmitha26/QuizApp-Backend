from django.db import models

# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    #if this method is not defined, then question.objects.all() would return something like <QuerySet [<Question: Question object (1)>]> which is not readable. hence we need this method
    def __str__(self):
        return self.question #returning the string value,this is the value that comes in admin panel when we create model.

class Choice(models.Model):
    choice_text = models.CharField(max_length=100)
    question = models.ForeignKey(Question, on_delete=models.CASCADE,null=True,blank=True)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text 

class Admin(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)