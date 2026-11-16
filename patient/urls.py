from rest_framework.routers import DefaultRouter
from django.urls import path,include
from  .views import PatientViewset,PatientDetail


urlpatterns=[

    path('list/', PatientViewset.as_view(), name='st'),
    path('list/<int:pk>/', PatientDetail.as_view(), name='pt'),
]