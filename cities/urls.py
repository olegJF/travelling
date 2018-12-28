from django.urls import path
from .views import home, CityDetailView, CityCreateView

urlpatterns = [
    path('detail/<int:pk>/', CityDetailView.as_view(), name='detail'),
    path('add/', CityCreateView.as_view(), name='add'),
    path('', home, name='home'),

]