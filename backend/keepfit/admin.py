from django.contrib import admin
from .models import KeepFit

class KeepFitAdmin(admin.ModelAdmin):
    list_display = ('title', 'goal_description', 'goal_completed')

# Register your models here.

admin.site.register(KeepFit, KeepFitAdmin)
# Register your models here.
