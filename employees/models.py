from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    job_title = models.CharField(max_length=100)
    hire_date = models.DateField()
    
    EMPLOYMENT_TYPE_CHOICES = [
        ('part_time', 'part_time'),
        ('full_time', 'full_time'),
    ]
    employment_type = models.CharField(max_length=10, choices=EMPLOYMENT_TYPE_CHOICES, default='full_time')

    def __str__(self):
        return self.name
