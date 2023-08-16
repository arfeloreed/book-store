from django.urls import path
from . import views


# urls
urlpatterns = [
    path("", views.index),
    path("<slug:slug>", views.book_info, name="book_info"),
]
