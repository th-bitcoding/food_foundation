from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
# from serializers import UserSerializers
# Create your views here.
def index(request):
    return render(request,'dashboard/home.html')

# class UserModelViewSet(viewsets.ModelViewSet):
#     serializer_class = UserSerializers

def about(request):
    return render(request,'about/about.html')

def product(request):
    return render(request,'product/product.html')

def contact(request):
    return render(request,'dashboard/contact.html')