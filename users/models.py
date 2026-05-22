
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager
)

import uuid


# Custom User Manager
class CustomUserManager(BaseUserManager):

    def create_user(self, username, email, password=None):

        if not username:
            raise ValueError("Username is required")

        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)

        user = self.model(
            username=username,
            email=email,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password):

        user = self.create_user(
            username=username,
            email=email,
            password=password
        )

        user.is_staff = True
        user.is_superuser = True
        user.is_active = True

        user.save(using=self._db)

        return user


# Custom User Model
class CustomUser(AbstractBaseUser, PermissionsMixin):

    uuid = models.UUIDField(
        verbose_name="User UUID",
        default=uuid.uuid4,
        editable=False,
        unique=True,
        help_text="Unique identifier for each user"
    )

    username = models.CharField(
        verbose_name="Username",
        max_length=100,
        unique=True,
        db_index=True,
        blank=False,
        help_text="Unique username for login"
    )

    email = models.EmailField(
        verbose_name="Email Address",
        max_length=255,
        unique=True,
        db_index=True,
        null=False,
        blank=False,
        help_text="User email address"
    )

    is_staff = models.BooleanField(
        verbose_name="Staff Status",
        default=False,
        help_text="Designates whether the user can access admin panel"
    )

    is_active = models.BooleanField(
        verbose_name="Active Status",
        default=True,
        help_text="Designates whether this user account is active"
    )

    created_at = models.DateTimeField(
        verbose_name="Created At",
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        verbose_name="Updated At",
        auto_now=True
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.username} - {self.email}"
