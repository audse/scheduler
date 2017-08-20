from django.contrib import admin
from .models import Worker, ScheduledWorker, Shift

# Register your models here.
admin.site.register(Worker)
admin.site.register(ScheduledWorker)
admin.site.register(Shift)