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
    added_date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)


LANGUAGE_CHOICES = (
    ('python', 'python'),
    ('java', 'java'),
    ('C', 'C'),
    ('C++', 'C++'),
    ('JavaScript', 'JavaScript')
)

STYLE_CHOICE = (
    ('friendly', 'friendly'),
    ('angry', 'angry')
)
class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICE, default='friendly', max_length=100)

    class Meta:
        ordering = ['created']