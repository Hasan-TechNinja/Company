from django.contrib import admin
from . models import Company, Snippet
# Register your models here.

admin.site.register(Snippet)
admin.site.register(Company)