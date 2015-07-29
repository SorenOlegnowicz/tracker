from django.contrib.auth.models import User
from django.db import models


class Parent(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    telephone = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name


class Child(models.Model):
    name = models.CharField(max_length=40)
    code = models.IntegerField()
    parent = models.ForeignKey(Parent, null=True)

    def __str__(self):
        return self.name

class Inquiry(models.Model):
    parent = models.ForeignKey(Parent)
    child = models.ForeignKey(Child)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.child.name


class Reply(models.Model):
    parent = models.ForeignKey(Parent)
    child = models.ForeignKey(Child, related_name='child')
    description = models.CharField(max_length=30)
    code = models.ForeignKey(Child, related_name='pin')
    # geocode = models.
