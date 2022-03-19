from django.urls import path
from .views import SignUpView, data_entry, result, get_all_users

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('data_entry/', data_entry, name='data_entry'),
    path('result/', result, name='result'),
    path('users/', get_all_users, name='get_all_users'),

]