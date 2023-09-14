from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.


class Student(models.Model):
  name = models.CharField(max_length=100)
  rollNo = models.CharField(max_length=10, unique=True)
  phone = models.CharField(max_length=15, unique=True)
  email = models.EmailField(max_length=100, unique=True)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name + ' - ' + self.rollNo
  

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
  if created: Token.objects.create(user=instance)


class Teacher(models.Model):
  name = models.CharField(max_length=100)
  subject = models.CharField(max_length=100)

  students = models.ManyToManyField(Student)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name + ' - ' + self.subject