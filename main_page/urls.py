from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main_template, name='main_page'),
]