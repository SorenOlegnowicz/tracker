from api import views
from django.conf.urls import url


urlpatterns = [
    url(r'^inquiry/(?P<pk>\d+)/', views.InquiryUpdateAPIView.as_view(), name='inquiry'),
    url(r'^reply/(?P<pk>\d+)/', views.ReplyListAPIView.as_view(), name='reply')
]