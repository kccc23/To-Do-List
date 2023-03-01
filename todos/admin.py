from django.contrib import admin
from .models import TodoList

# Register your models here.
@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "id",
    )