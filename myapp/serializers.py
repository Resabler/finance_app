from rest_framework import serializers
from .models import Transaction,Category,Budget
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError

class Transactionserializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    class Meta:
        model = Transaction
        fields = ('username','category','amount','transaction_type','date','description')
    def create(self,validated_data):
        username=validated_data.pop('username')
        try:
            user=User.objects.get(username=username)
        except User.DoesNotExist:
            raise ValidationError({"username":"User doesnt exist"})
        transaction=Transaction.objects.create(user=user,**validated_data)
        return transaction
    def to_representation(self, instance):
        representation= super().to_representation(instance)
        representation['username']=instance.user.username
        return representation

class Categoryserializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=('__all__')

class Budgetserializer(serializers.ModelSerializer):
    class Meta:
        model=Budget
        fields=('__all__')        
