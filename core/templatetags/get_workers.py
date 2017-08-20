from django.template import Library

from core.models import Worker

register = Library()

@register.filter(name="get_workers")
def get_workers(value):
	workers = Worker.objects.all().order_by('name')
	return workers