from django.db import models

class KeepFit(models.Model):
    title = models.CharField(max_length=100)
    goal_description = models.TextField()
    goal_completed = models.BooleanField(default=False)


def _str_(self):
        return self.title

# Create your models here.
