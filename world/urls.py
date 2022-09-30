from django.urls import path
from .views import MsgListView, MsgCreateView,MsgDetailView, MsgUpdateView, MsgDeleteView

urlpatterns = [
    path("list/", MsgListView.as_view(), name="msg_list"),
    path("new/", MsgCreateView.as_view(), name="msg_new"),
    path("<int:pk>/", MsgDetailView.as_view(), name="msg_detail"),
    path("<int:pk>/edit/", MsgUpdateView.as_view(), name="msg_edit"),
    path("<int:pk>/delete/", MsgDeleteView.as_view(), name="msg_delete"),
]