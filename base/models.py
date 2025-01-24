from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    
    CONDITION_CHOICES = [
        ('new', 'New'),
        ('good', 'Good'),
        ('used', 'Used'),
    ]

    seller = models.ForeignKey(User, on_delete=models.CASCADE)  # Linking to the User model
    
    name = models.CharField(max_length=200, blank=False)  # Item name

    price = models.IntegerField(blank=False)  # Item price

    picture = models.ImageField(upload_to='items/', blank=False)  # Image upload path

    condition = models.CharField(
        max_length=15,
        choices=CONDITION_CHOICES,
        default='new',
        blank=False
    ) 

    liked = models.ManyToManyField(User, related_name="liked_items", blank=True)

    def __str__(self):
        return self.name