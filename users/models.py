from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Additional fields
    role = models.CharField(max_length=50, choices=[
        ('admin', 'Admin'),
        ('primary_worker', 'Primary Worker'),
        ('manager', 'Manager'),
        ('vet', 'Vet'),
        ('auditor', 'Auditor')
    ])
    last_login = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',
        blank=True
    )
