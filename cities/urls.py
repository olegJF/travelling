from django.urls import path
from .views import home, CityDetailView

urlpatterns = [
    path('detail/<int:pk>/', CityDetailView.as_view(), name='detail'),
    path('', home, name='home'),

]