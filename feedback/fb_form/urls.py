from django.conf.urls import url

from . import views

app_name = 'fb_form'
urlpatterns = [
    url(r'^$', views.index, name='home'),
]