from django.contrib import admin
from .models import Parent, Child, Inquiry, Reply

# Register your models here.

admin.site.register(Parent)
admin.site.register(Child)
admin.site.register(Inquiry)
admin.site.register(Reply)


