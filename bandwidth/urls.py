from django.urls import include, path
from bandwidth import views

urlpatterns = [
    path('', views.simple_view)
]