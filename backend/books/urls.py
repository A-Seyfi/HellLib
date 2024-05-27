from django.urls import path

from . import views

urlpatterns = [
    path("", views.BooksAPIView.as_view()),
    path("search/<str:title>", views.SearchBooks.as_view()),
    path("borrow", views.BorrowBookAPIView.as_view()),
    path("repossess", views.RepossessBookAPIView.as_view())
]
