from django.urls import path, include

from .views import UserListCreateView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user-list'),
]
