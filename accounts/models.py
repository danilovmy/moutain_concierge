from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom user model for future extensibility."""
    # Placeholder for future fields (e.g., role, phone)
    pass
