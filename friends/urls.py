from django.urls import path
from .views import ShareListView, ShareCreateView,ShareDetailView, ShareUpdateView, ShareDeleteView

urlpatterns = [
    path("list/", ShareListView.as_view(), name="share_list"),
    path("new/", ShareCreateView.as_view(), name="share_new"),
    path("<int:pk>/", ShareDetailView.as_view(), name="share_detail"),
    path("<int:pk>/edit/", ShareUpdateView.as_view(), name="share_edit"),
    path("<int:pk>/delete/", ShareDeleteView.as_view(), name="share_delete"),
]