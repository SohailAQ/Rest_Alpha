from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from django.db import transaction
from dj_rest_auth.serializers import LoginSerializer as RestAuthLoginSerializer
from PIL import Image

from users.models import GENDER_SELECTION
from users.models import CustomUser


class CustomRegisterSerializer(RegisterSerializer):
    gender = serializers.ChoiceField(choices=GENDER_SELECTION)
    phone_number = serializers.CharField(max_length=30)
    image = serializers.ImageField()

    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.gender = self.data.get('gender')
        user.phone_number = self.data.get('phone_number')
        user.image = self.data.get('image')

        user.save()
        return user


class CustomUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'pk',
            'email',
            'phone_number',
            'gender',
            'image',
        )
        read_only_fields = ('pk', 'email', 'gender',)


class LoginSerializer(RestAuthLoginSerializer):
    username = None
