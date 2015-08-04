from django.shortcuts import render
from rest_framework import generics, serializers

from beacon.models import Inquiry

class InquirySerializer(serializers.ModelSerializer):

    class Meta:
        model = Inquiry

class InquiryUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = InquirySerializer
    queryset = Inquiry.objects.all()

    def dispatch(self, request, *args, **kwargs):
        print(request)
        print(request.body)
        return super().dispatch(request,*args,**kwargs)