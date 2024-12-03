from rest_framework import serializers
from .models import (Deposit, Saving, DepositOptions, SavingOptions,)

class DepositSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = Deposit
        fields = '__all__'
        
class SavingSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = Saving
        fields = '__all__'

class DepositOptionsSerializer(serializers.ModelSerializer) : 
    class Meta : 
        product = serializers.PrimaryKeyRelatedField(read_only=True)
        model = DepositOptions
        fields = '__all__'
        
class SavingOptionsSerializer(serializers.ModelSerializer) : 
    class Meta : 
        product = serializers.PrimaryKeyRelatedField(read_only=True)
        model = SavingOptions
        fields = '__all__'