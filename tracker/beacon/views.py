from datetime import timedelta
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.shortcuts import render
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from .models import Parent, Child, Inquiry, Reply
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.shortcuts import render_to_response
from django.template import RequestContext


def reply(request, pk):
    var = Inquiry.objects.get(pk=pk)
    context = {'inquiry': var}
    if request.POST:  # Is there post data in the request?
        if request.POST['pin'] == var.child.pin:  # checks to see if pin is accurate
            Reply.objects.create(inquiry=var,
                                 description=request.POST['description'],
                                 position=request.POST['position'])
            return redirect('success')
        else:
            context['errors'] = "Invalid Pin Number"

    return render_to_response("reply3.html", context, context_instance=RequestContext(request))


def home(request):
    context = {}
    return render_to_response("home_page.html", context, context_instance=RequestContext(request))


class Registration(generic.FormView):
    template_name = 'registration/create_user.html'
    form_class = UserCreationForm
    success_url = '/profile_update'

    #  auto-login
    def form_valid(self, form):
      form.save()
      username = self.request.POST['username']
      password = self.request.POST['password1']
      user = authenticate(username=username, password=password)
      login(self.request, user)
      Parent.objects.create(user=user)
      return super().form_valid(form)


class ParentDetailView(generic.DetailView):
    model = Parent
    template_name = 'parent_detail.html'

    def get_object(self):
        return self.request.user.parent


class ParentUpdateView(generic.UpdateView):
    model = Parent
    fields = ['first_name', 'last_name', 'telephone']
    template_name = 'parent_update.html'
    success_url = '/profile'

    def get_object(self):
        return self.request.user.parent


class ParentCreateView(generic.CreateView):
    model = Parent
    fields = ['first_name', 'last_name', 'telephone']
    template_name = "parent_form.html"
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ChildCreateView(generic.CreateView):
    model = Child
    fields = ['name', 'pin', 'telephone']
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


def child_detail(request, pk):
    obj = Child.objects.get(pk=pk)
    latest = Inquiry.objects.filter(child=obj).order_by('id').reverse()[0]
    inquiries = Inquiry.objects.filter(child=obj).count()
    replies = len(obj.replies())
    if replies:
        percentage = round((100 * (replies / inquiries)), 2)
    else:
        percentage = 0
    stamps = Inquiry.objects.filter(child=obj).values_list('replystamp', flat=True)
    delta = timedelta(days=0)
    for stamp in stamps:
        if stamp:
            delta += stamp
    average = delta/len(stamps)
    second = average.seconds % 60
    minutes = average.seconds // 60
    if minutes > 60:
        adjusted = minutes % 60
    else:
        adjusted = minutes * 1
    hours = minutes // 60
    context = {'obj': obj, 'latest': latest, 'inquiries': inquiries,
               'replies': replies, 'percentage': percentage, 'adjusted': adjusted,
               'hours': hours, 'minutes': minutes, 'seconds': second}

    return render_to_response("child_detail.html", context, context_instance=RequestContext(request))


class InquiryCreateView(generic.CreateView):
    model = Inquiry
    fields = ['child', 'description']
    template_name = 'inquiry_form.html'
    success_url = '/inquiry'

    # Filters the 'child' field
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['child'].queryset = Child.objects.filter(parent=self.request.user.parent)
        return form

    def form_valid(self, form):
        form.instance.parent=self.request.user.parent
        return super().form_valid(form)

# class InquiryListView(generic.ListView):
#     model = Inquiry
#     template_name = 'inquiry_form.html'
#
#
# class InquiryDetailView(generic.DetailView):
#     model = Inquiry
#     template_name = 'inquiry_detail2.html'


def inquiry_detail(request, pk):
    obj = Inquiry.objects.get(pk=pk)
    diff = obj.replystamp
    seconds = diff.seconds % 60
    minutes = diff.seconds // 60
    if minutes > 60:
        adjusted = minutes % 60
    else:
        adjusted = minutes * 1
    hours = minutes // 60
    context = {'obj': obj, 'hours': hours, 'minutes': minutes, 'seconds': seconds, 'adjusted': adjusted}
    return render_to_response("inquiry_detailT2.html", context, context_instance=RequestContext(request))

def success(request):
    context = {}
    return render_to_response("success.html", context, context_instance=RequestContext(request))