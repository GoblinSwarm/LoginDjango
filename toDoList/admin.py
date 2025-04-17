from django.contrib import admin
from .models import Task, Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'location')

admin.site.register(Task)



