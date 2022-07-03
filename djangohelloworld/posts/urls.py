from django.urls import path
from .views import MessageBoardPageView

urlpatterns = [
    path('', MessageBoardPageView.as_view(), name='messageboard')
]
