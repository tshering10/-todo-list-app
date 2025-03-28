from django.contrib import admin
from .models import Task
# Register your models here.

class TaskAdmin(admin. ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'completed')
    list_filter = ('completed', 'created_at')
admin.site.register(Task,TaskAdmin)