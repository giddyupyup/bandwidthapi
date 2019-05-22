from django.urls import include, path
from bandwidth import views

urlpatterns = [
    path('bandwidth/',
         views.BandwidthList.as_view(),
         name=views.BandwidthList.name),
    path('bandwidth/<int:pk>/',
         views.BandwidthDetail.as_view(),
         name=views.BandwidthDetail.name),
    path('',
         views.ApiRoot.as_view(),
         name=views.ApiRoot.name),
]