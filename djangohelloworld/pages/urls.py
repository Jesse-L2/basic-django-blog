from django.urls import path

from .views import HomePageView, AboutPageView

urlpatterns = [
    # if the user requests the homepage represented by an empty string, use the view called homePageView
    # name='home' is optional for later reference
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
]