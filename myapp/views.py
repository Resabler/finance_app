from rest_framework.pagination import PageNumberPagination
class Custompagination(PageNumberPagination):
    page=10
    custom_page_size=10
    max_page_size=100



from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics,permissions
from .models import Transaction,Category,Budget
from. serializers import Transactionserializer,Categoryserializer,Budgetserializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import NotFound
@csrf_exempt
def register(request):
    if request.method=='POST':
        data=json.loads(request.body)
        username=data.get('username')
        password=data.get('password')
        email=data.get('email')
        if not username or not email or not password:
            return JsonResponse({"error":"all fields are mandatory"},status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({"error":"this user already exists"},status=400)
        user=User.objects.create(
            username=username,password=password,email=email
        )
        return JsonResponse({"message":"user created successfully"},status=201)


class Transactionlistcreateview(generics.ListCreateAPIView):
    queryset=Transaction.objects.all()
    serializer_class=Transactionserializer
    pagination_class=Custompagination
    filter_backends=[DjangoFilterBackend]

class Transactionupdateretrieveview(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=Transactionserializer
    def get_object(self):
        username=self.kwargs.get('username')
        try:
            user=User.objects.get(username=username)
        except User.DoesNotExist:
            raise NotFound({"error":"The user doesnt exists"})
        return Transaction.objects.get(user=user)
    pagination_class=Custompagination
    filter_backends=[DjangoFilterBackend]

class Transactionlistview(generics.ListAPIView):
    serializer_class=Transactionserializer
    def get_queryset(self):
        username=self.kwargs['username']
        date=self.kwargs['date']
        try:
            user=User.objects.get(username=username)
        except User.DoesNotExist:
            raise NotFound("User not found")
        return Transaction.objects.filter(user=user,date=date)   
#to define the api endpoint by accessing the username alone

        
            
    