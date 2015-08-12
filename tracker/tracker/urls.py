"""tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout

from beacon import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home, name='home'),
    url(r'^api/', include('api.urls')),
    url(r'^registration/$', views.Registration.as_view(), name="registration"),
    url(r'^registration/parent_create/', views.ParentCreateView.as_view(), name="parent_create"),
    url(r'^profile/', views.ParentDetailView.as_view(), name="parent_detail"),
    url(r'^profile_update/', views.ParentUpdateView.as_view(), name="parent_update"),
    url(r'^accounts/login/', login, name="login"),
    url(r'^logout/', logout, {'next_page': '/'}, name="logout"),
    url(r'^child_create/$', views.ChildCreateView.as_view(), name='child_create'),
    url(r'^child_list/$', views.ChildListView.as_view(), name='child_list'),
    url(r'^child/(?P<pk>\d+)/', views.child_detail, name="child_detail"),
    url(r'^inquiry/$', views.InquiryCreateView.as_view(), name='inquiry_create'),
    url(r'^inquiry/(?P<pk>\d+)/', views.inquiry_detail, name='inquiry_detail'),
    url(r'^test/(?P<pk>\d+)/', views.reply, name='reply'),
    url(r'^success/', views.success, name="success")
]
