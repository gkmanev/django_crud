from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import SoftDeletionManager#,CustomUserManager
from django.utils import timezone


class SoftDeletionModel(models.Model):

    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    objects = SoftDeletionManager()
    all_objects = SoftDeletionManager(alive_only=False)

    class Meta:
        abstract = True

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()



class CustomUser(AbstractUser):
    #deleted_at = models.DateTimeField(blank=True, null=True)

    email = models.EmailField(unique=True)
    location = models.CharField(max_length=30, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)

    #objects = CustomUserManager()
    #all_objects = CustomUserManager(alive_only=False)

    # def delete(self):
    #     self.deleted_at = timezone.now()
    #     self.save()


    def __str__(self):
        return self.email

class Client(SoftDeletionModel):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ClientContact(SoftDeletionModel):
    PHONE = 'P'
    EMAIL = 'M'
    ADDRESS = 'A'

    CONTACT_TYPE = [
        (PHONE, 'phone'),
        (EMAIL, 'email'),
        (ADDRESS, 'address'),

    ]
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    type = models.CharField(
        max_length=2,
        choices=CONTACT_TYPE,
        default=PHONE,
    )
