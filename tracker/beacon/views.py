from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.shortcuts import render
from django.views import generic
from .models import Parent, Child, Inquiry, Reply
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.shortcuts import render_to_response
from django.template import RequestContext


def home(request):
    context ={}
    return render_to_response("base.html", context, context_instance=RequestContext(request))


class Registration(generic.FormView):
    template_name = 'registration/create_user.html'
    form_class = UserCreationForm
    success_url = 'parent_create'

    #  auto-login
    def form_valid(self, form):
      form.save()
      username = self.request.POST['username']
      password = self.request.POST['password1']
      user = authenticate(username=username, password=password)
      login(self.request, user)
      return super(Registration, self).form_valid(form)


class ParentCreateView(generic.CreateView):
    model = Parent
    fields = ['first_name', 'last_name', 'telephone']
    template_name = "parent_form.html"
    success_url = '/'

    def form_valid(self, form):
        print('hello')
        form.instance.user = self.request.user
        return super().form_valid(form)

class ChildCreateView(generic.CreateView):
    model = Child
    fields = ['name', 'code']
    template_name = 'child_form.html'
    success_url = '/child_list'

    def form_valid(self, form):
        form.instance.parent=self.request.user.parent
        return super().form_valid(form)


class ChildListView(generic.ListView):
    model = Child
    template_name = "child_list.html"

    """def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['the pk'] = self.kwargs.get('pk')
        return context"""

    def get_queryset(self):
        parent = Parent.objects.get(user=self.request.user)
        return Child.objects.filter(parent=parent)


class InquiryCreateView(generic.CreateView):
    model = Inquiry
    fields = ['child', 'description']
    template_name = 'inquiry_form.html'
    success_url = 'inquiry_form.html'

    # Filters the 'child' field
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['child'].queryset = Child.objects.filter(parent=self.request.user.parent)
        return form

    def form_valid(self, form):
        form.instance.parent=self.request.user.parent
        return super().form_valid(form)

class InquiryListView(generic.ListView):
    model = Inquiry
    template_name = 'inquiry_form.html'
