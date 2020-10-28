from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse #For get_absolute_url()

class Post(models.Model):
    book_name = models.CharField(max_length=35)
    book_description = models.TextField(max_length=50)
    book_image = models.ImageField(default='book.jpg', upload_to='book_pics')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^\d{10}$', message="Check your format of phone number. Up to 10 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=10, default="0000000000") # validators should be a list
    
    def __str__(self):
        return self.book_name
    
    def save(self):
        super().save()
        
        img = Image.open(self.book_image.path)
        
        if img.height > 400 or img.width > 400:
            output_size = (474, 447)
            img.thumbnail(output_size)
            img.save(self.book_image.path)
    
    def get_absolute_url(self):
        return reverse('index')