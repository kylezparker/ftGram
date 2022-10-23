from django.urls import path
from friends.views import ShowProfilePageView 
from .views import ShareListView, ShareCreateView,ShareDetailView, ShareUpdateView, ShareDeleteView, Profile, LikeView

urlpatterns = [
    path("list/", ShareListView.as_view(), name="share_list"),
    path("new/", ShareCreateView.as_view(), name="share_new"),
    path('profile/', Profile, name='users_profile'),
    path("<int:pk>/", ShareDetailView.as_view(), name="share_detail"),
    path("<int:pk>/edit/", ShareUpdateView.as_view(), name="share_edit"),
    path("<int:pk>/delete/", ShareDeleteView.as_view(), name="share_delete"),
    path("<int:pk>/profile/", ShowProfilePageView.as_view(), name="show_profile_page"),
    path ("<int:pk>like/", LikeView, name="post_likes"),

]