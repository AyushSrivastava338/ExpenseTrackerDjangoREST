from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Expense, CustomUser


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'password', 'full_name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create(full_name=validated_data['full_name'],
                                             email=validated_data['email'])

        user.set_password(validated_data['password'])
        user.save()

        return user

