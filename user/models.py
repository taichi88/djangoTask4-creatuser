from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)  # Unique username
    email = models.EmailField(unique=True)  # Unique email address
    password = models.CharField(max_length=128)  # Hashed password
    date_of_birth = models.DateField(null=True, blank=True)  # User's date of birth
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)  # User's phone number
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)  # Profile picture
    bio = models.TextField(null=True, blank=True)  # Short biography
    address = models.CharField(max_length=255, null=True, blank=True)  # User's address
    is_verified = models.BooleanField(default=False)  # Verification status
    created_at = models.DateTimeField(auto_now_add=True)  # Account creation timestamp
    updated_at = models.DateTimeField(auto_now=True)  # Last updated timestamp

    def __str__(self):
        return self.username  # Or return self.email if preferred
