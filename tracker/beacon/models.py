from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from twilio.rest import TwilioRestClient
from geoposition.fields import GeopositionField


class Parent(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    telephone = models.CharField(max_length=12)

    def __str__(self):
        return self.first_name


class Child(models.Model):
    name = models.CharField(max_length=40)
    code = models.IntegerField()
    parent = models.ForeignKey(Parent, null=True)
    telephone = models.CharField(max_length=12)


    def __str__(self):
        return self.name

class Inquiry(models.Model):
    parent = models.ForeignKey(Parent)
    child = models.ForeignKey(Child)
    description = models.CharField(max_length=50)
    reply = models.CharField(max_length=50)
    position = GeopositionField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.child.name


class Status(models.Model):
    inquiry = models.OneToOneField(Inquiry)
    time = models.DateTimeField(auto_now_add=True)


#class Reply(models.Model):
    #description = models.CharField(max_length=30)
    #inquiry = models.OneToOneField(Inquiry)
    ##code = models.ForeignKey(Child, related_name='pin')
    #position = GeopositionField()


client = TwilioRestClient()  # The SID and Auth Token are stored as environment variables

@receiver(post_save, sender=Inquiry)
def create_sms(sender, instance, created=False, **kwargs):
    if created:
        print(instance.child.telephone)
        client.messages.create(to=instance.child.telephone, from_="+12513331231", body=instance.description + ' 10.0.10.67:8000/test/' + str(instance.id))
