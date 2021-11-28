from django.urls import path
from .views import BookList, BookDetail

urlpatterns = [
    
    path('api/books/', BookList.as_view()),
    path('api/books/{id}', BookDetail.as_view())
]z