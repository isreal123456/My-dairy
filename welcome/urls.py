from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.homeview.as_view(), name="home"),
    path("detail/<int:pk>/", views.detailview.as_view(), name="detail"),
    path("list/", views.listview.as_view(), name="list1"),
    path("create/", views.Createview.as_view(), name="create"),

]


