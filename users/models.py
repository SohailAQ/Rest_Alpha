from django.db import models
from django.contrib.auth.models import AbstractUser


GENDER_SELECTION = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('NS', 'Not Specified'),
]


class CustomUser(AbstractUser):
    # email attribute is inherited from AbstractUser
    gender = models.CharField(max_length=20, choices=GENDER_SELECTION)
    phone_number = models.CharField(max_length=30)
    image = models.ImageField(default='user_default_m.png', upload_to='image/', blank=True, null=True)

    def __str__(self):
        return self.email

