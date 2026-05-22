from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager
)


# Organization Model
class Organization(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()

    website = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True)

    logo = models.ImageField(upload_to='organization_logos/', blank=True, null=True)

    established_date = models.DateField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.pk and Organization.objects.exists():
              raise ValueError("Only one organization instance is allowed")
        super().save(*args, **kwargs)