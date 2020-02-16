from django.contrib import admin

from .models import TodoTask


class TodoTaskModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'created', 'due_by')


admin.site.register(TodoTask, TodoTaskModelAdmin)
