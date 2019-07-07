# django_app/admin.py
from django.contrib import admin
from .models import Quote

admin.site.register(Quote)
