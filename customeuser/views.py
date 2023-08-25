from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import UserSerializers
from rest_framework.response import Response
from .models import *
import random
import string
from django.conf import settings
from django.core.mail import send_mail
from rest_framework import status

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

class UserApiView(APIView):
    permission_classes = []

    def get(self, request, *args, **kwargs):
        queryset = CustomeUser.objects.all()
        serializer = UserSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            print('********', email)

            # Generate password
            username = email.split('@')[0]
            password = username + ''.join(random.choice(string.digits) for _ in range(3))
            print('*' * 5, password)

            # Create and save the user
            user = serializer.save(username=username, password=password, user_type=2)
            user.set_password(password)
            user.save()

            # Send email
            subject = "Auto Generate Email"
            message = f'Hello! Your Username is: {username} and your password is: {password}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, email_from, recipient_list)

            return Response({'detail': 'User created successfully', 'username': username}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
