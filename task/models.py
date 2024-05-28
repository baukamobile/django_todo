from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100, blank=False)
    comment = models.TextField(max_length=150, blank=True)
    created_time = models.DateField(auto_now_add=True)
    is_done = models.BooleanField(default=False, blank=True)
    photo = models.ImageField(blank=True, null=True)
    deleted_time = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title
