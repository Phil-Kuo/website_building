from django.contrib import admin

#yimin added
from rango.models import Category, Page

# Register your models here.
admin.site.register(Category)
admin.site.register(Page)
