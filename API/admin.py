from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import *
# Register your models here.
class PostAdmin(ModelAdmin):
    list_display = ['author','title','created_at']
    list_filter = ['updated_at']
admin.site.register(Post,PostAdmin)