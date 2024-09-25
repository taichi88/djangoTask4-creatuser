from django.db import models

class User(models.Model):
    name = models.CharField(max_length=150)  # Unique username
    username = models.CharField(max_length=150)  # Unique username


    def __str__(self):

        
        return f"{self.username} {self.name} "  # Or return self.email if preferred
