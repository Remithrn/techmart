from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Profile(AbstractUser):
    phone_number = models.CharField(max_length=15)

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name='profile_set',  # Change 'profile_set' to a name of your choice
        related_query_name='profile',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='profile_set',  # Change 'profile_set' to a name of your choice
        related_query_name='profile',
    )

    def __str__(self):
        return self.username