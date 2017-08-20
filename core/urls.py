"""scheduler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home_page, name='home_page'),
	url(r'^schedule/$', views.set_schedule_page, name='set_schedule_page'),
	url(r'^schedule/add/$', views.add_shift, name='add_shift'),
	url(r'^schedule/delete/(?P<pk>[0-9]+)$', views.delete_shift, name='delete_shift'),
	url(r'^add/$', views.add_worker_page, name='add_worker_page'),
	url(r'^add/processing/$', views.add_worker, name='add_worker'),
	url(r'^schedule/generate/$', views.generate_schedule, name='generate_schedule'),
	url(r'^schedule/delete/$', views.delete_schedule, name='delete_schedule'),
]
