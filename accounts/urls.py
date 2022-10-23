from django.urls import path

from friends.views import ShowProfilePageView 
from .views import SignUpView, UserEditView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile'),
]




