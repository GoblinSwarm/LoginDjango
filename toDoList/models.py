from django.db import models

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='tasks')
    creation_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    