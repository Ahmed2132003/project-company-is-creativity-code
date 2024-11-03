from django.db import models

class Clintes(models.Model):
    id=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    number_of_transection = models.CharField(max_length=100)
    first_transction = models.DateField()

    def __str__(self):
        return self.name