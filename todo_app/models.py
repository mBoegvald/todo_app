from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    text = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    
    @classmethod
    def create_todo(cls, user, text):
        todo = cls()
        todo.user = user
        todo.text = text
        todo.save()

    def change_status(self):
        self.status = not self.status
        self.save()
        
    def __str__(self):
        return f"{self.text} - {self.status}"

class Pdf(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    document = models.FileField(null=True, blank=True)

    @classmethod
    def create_pdf(cls, user, document):
        pdf = cls()
        pdf.user = user
        pdf.document = document
        pdf.save()
    
    # def update_pdf(self, document):
    #     self.document = document
    #     self.save()


    def __str__(self):
        return f"{self.user} - {self.document}"