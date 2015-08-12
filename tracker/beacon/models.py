from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from twilio.rest import TwilioRestClient
from geoposition.fields import GeopositionField
from .validators import validate_pin
from django.core.validators import MaxLengthValidator, MinLengthValidator


class Parent(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    telephone = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.first_name


class Child(models.Model):
    name = models.CharField(max_length=40)
    pin = models.CharField(max_length=4,validators=[validate_pin, MinLengthValidator(4), MaxLengthValidator(4)])
    parent = models.ForeignKey(Parent, null=True)
    telephone = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    def replies(self):
        #obj = self.objects.get
        reply_list = []
        for inquiry in self.inquiry_set.all():
            try:
                reply_list.append(inquiry.reply)
            except ObjectDoesNotExist:
                pass
        return reply_list

class Inquiry(models.Model):
    parent = models.ForeignKey(Parent)
    child = models.ForeignKey(Child)
    description = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)
    replystamp = models.DurationField(blank=True, null=True)
    relative_location = GeopositionField()

    def __str__(self):
        return self.child.name


class Reply(models.Model):
    description = models.CharField(max_length=30)
    inquiry = models.OneToOneField(Inquiry, primary_key=True)
    #code = models.ForeignKey(Child, related_name='pin')
    position = GeopositionField(blank=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.inquiry.child.name


client = TwilioRestClient()  # The SID and Auth Token are stored as environment variables

@receiver(post_save, sender=Inquiry)
def create_sms(sender, instance, created=False, **kwargs):
    if created:
        print(instance.child.telephone)
        client.messages.create(to='+1' + instance.child.telephone,
                               from_="+12513331231",
                               body=instance.description + ' 10.0.10.67:8000/test/' + str(instance.id))

@receiver(post_save, sender=Reply)
def create_replystamp(sender, instance, created=False, **kwargs):
    if created:
        diff = instance.time - instance.inquiry.time
        instance.inquiry.replystamp = diff
        instance.inquiry.save()
