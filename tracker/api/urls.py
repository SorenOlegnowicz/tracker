from api import views
from django.conf.urls import url


urlpatterns = [
    url(r'^inquiry/(?P<pk>\d+)/', views.InquiryUpdateAPIView.as_view(), name='child_reply')
]