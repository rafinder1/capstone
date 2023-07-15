from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    class Meta:
        db_table = 'auth_user'
        swappable = 'AUTH_USER_MODEL'


class Projects(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    requirements = models.CharField(max_length=100, blank=True)
    technology = models.CharField(max_length=100)
    video = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title
