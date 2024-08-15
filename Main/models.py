from django.db import models

# Create your models here.


type_choice = (
    ('IT','IT'),
    ('Computer', 'Computer'),
    ('Mobile','Mobile')

)

class Company(models.Model):
    company_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    about = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices= type_choice)
    added_date = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)

    