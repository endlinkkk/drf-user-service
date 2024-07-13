from django.db import models


from django.contrib.auth.models import (
    PermissionsMixin,
    BaseUserManager,
    AbstractBaseUser,
)


class UserProfileManager(BaseUserManager):
    """Manager for User profiles"""

    def create_user(self, email: str, name: str, password: str = None) -> "UserProfile":
        """Create a new User profile"""
        if not email:
            raise ValueError("User must have an email address")

        email = self.normalize_email(email)
        user: AbstractBaseUser = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email: str, name: str, password: str) -> "UserProfile":
        """Create and save a new superuser"""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model users in the system"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = (
        "email"  # Переопределение стандартной системы авторизации по username
    )
    REQUIRED_FIELDS = [
        "name"
    ]  # Определеяет те вопросы, которые Django задает при команде createsuperuser

    def get_full_name(self) -> str:
        return self.name

    def get_short_name(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.email
