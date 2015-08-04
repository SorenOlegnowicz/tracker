from django import forms
from .models import Inquiry, Parent, Child


class InquiryForm(forms.Form):
    parent = Parent.objects.get(user=self.request.user)
    child = forms.ModelChoiceField(queryset=Child.objects.filter(parent=parent))

    class Meta:
        model = Inquiry
        fields = ['description']


class ReplyForm(forms.Form):
    pass
