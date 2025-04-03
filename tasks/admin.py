from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'priority', 'status', 'due_date', 'created_date')
    list_filter = ('priority', 'status', 'user')
    search_fields = ('title', 'description')
    date_hierarchy = 'due_date'
    ordering = ('-created_date',)
