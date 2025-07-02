from rest_framework.routers import DefaultRouter
from .views import ComplaintViewSet
from django.urls import path, include
router = DefaultRouter()
router.register(r'', ComplaintViewSet)
from django.shortcuts import render

urlpatterns = [
    path('api/', include(router.urls)),
    path('', lambda request: render(request, 'complaints/complaints.html')),  # view with JS
]