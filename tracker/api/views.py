from django.shortcuts import render
from rest_framework import generics, serializers

from beacon.models import Inquiry, Reply

class InquirySerializer(serializers.ModelSerializer):

    class Meta:
        model = Inquiry


class ReplySerializer(serializers.ModelSerializer):

    class Meta:
        model = Reply


class InquiryUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = InquirySerializer
    queryset = Inquiry.objects.all()

    def dispatch(self, request, *args, **kwargs):
        print(request)
        print(request.body)
        return super().dispatch(request,*args,**kwargs)


class ReplyListAPIView(generics.RetrieveAPIView):
    serializer_class = ReplySerializer
    queryset = Reply.objects.all()