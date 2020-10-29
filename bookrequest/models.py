from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone


class BookRequest(models.Model):
    book_name = models.CharField(max_length=40, unique=True)
    semester = models.CharField(max_length=1, validators=[RegexValidator(regex=r'^[1-8]$', message="Invalid Semester.")])
    student_name = models.CharField(max_length=15)
    date_posted = models.DateTimeField(default=timezone.now)
    contact_regex = RegexValidator(regex=r'^\d{10}$', message="Check your format of phone number. Up to 10 digits allowed.")
    contact_number = models.CharField(validators=[contact_regex], max_length=10, default="0") # validators should be a list
    
    def __str__(self):
        return f'{self.student_name} Requested'