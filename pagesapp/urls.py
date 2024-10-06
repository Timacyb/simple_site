from django.urls import path
from .views import ContactUsView, HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contact/', ContactUsView.as_view(), name='contact'),
]