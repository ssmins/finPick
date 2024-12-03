from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(required=False, allow_blank=True, max_length=100)
    age = serializers.IntegerField(required=False, allow_null=True)
    salary = serializers.CharField(required=False, allow_blank=True, max_length=20)
    depositAmount = serializers.CharField(required=False, allow_blank=True, max_length=20)
    depositPeriod = serializers.CharField(required=False, allow_blank=True, max_length=20)
    savingsAmount = serializers.CharField(required=False, allow_blank=True, max_length=20)
    savingsPeriod = serializers.CharField(required=False, allow_blank=True, max_length=20)

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'nickname': self.validated_data.get('nickname', ''),
            'age': self.validated_data.get('age', None),
            'salary': self.validated_data.get('salary', ''),
            'depositAmount': self.validated_data.get('depositAmount', ''),  # 수정
            'depositPeriod': self.validated_data.get('depositPeriod', ''),  # 수정
            'savingsAmount': self.validated_data.get('savingsAmount', ''),  # 수정
            'savingsPeriod': self.validated_data.get('savingsPeriod', ''),  # 수정
        }

    def save(self, request):
        user = super().save(request)
        print(f"DEBUG: 요청 데이터 - {request.data}")
        print(f"DEBUG: save - validated_data: {self.validated_data}")

        user.nickname = self.validated_data.get('nickname', '') 
        user.age = self.validated_data.get('age', '') 
        user.salary = self.validated_data.get('salary', '') 
        user.depositAmount = self.validated_data.get('depositAmount', '')  # 수정
        user.depositPeriod = self.validated_data.get('depositPeriod', '')  # 수정
        user.savingsAmount = self.validated_data.get('savingsAmount', '')  # 수정
        user.savingsPeriod = self.validated_data.get('savingsPeriod', '')  # 수정
        user.save()
        print(f"DEBUG: 사용자 저장 후 - nickname: {user.nickname}, deposit_amount: {user.depositAmount}, savings_period: {user.savingsPeriod},age: {user.age}")
        return user

class CustomUserDetailsSerializer(UserDetailsSerializer): 
    class Meta: 
        model = UserModel
        fields = (
            'pk', 'username', 'email', 'first_name', 'last_name', 
            'nickname', 'age', 'salary', 
            'depositAmount', 'depositPeriod', 
            'savingsAmount', 'savingsPeriod',
            # 'liked_deposits', 'liked_savings',
        )
        read_only_fields = ('email', 'liked_deposits', 'liked_savings')
