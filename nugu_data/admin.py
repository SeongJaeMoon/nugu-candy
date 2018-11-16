from django.contrib import admin
from .models import Calorie

admin.register(Calorie)(admin.ModelAdmin)