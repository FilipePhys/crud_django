from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class CustomUser(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    profile_img = models.ImageField(upload_to='profileimg', null=True, blank=True)

    def __str__(self):
        return self.username


