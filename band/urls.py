from django.urls import path

from . import views

urlpatterns = [
    path('', views.indexband, name='indexband'),
    path('<int:band_id>/', views.detail, name = 'detail')
]
