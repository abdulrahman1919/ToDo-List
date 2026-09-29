from django.db import models

# Create your models here.
class Todo(models.Model):
    title=models.CharField(max_length=13)
    discript=models.CharField(max_length=100)
    status=models.CharField(max_length=10 , default="Pending")
    addtime=models.TimeField()

    def __str__(self):
        return self.title
