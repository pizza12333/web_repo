from django.conf.urls import url, include
from django.contrib import admin
from rest_api import views
from rest_api.serializers import ChickenSerializer

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', views.ChickenViewSet.as_view()),
    url(r'', include('main_page.urls')),
]