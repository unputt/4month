from django.urls import path

from . import views

urlpatterns = [
    path('books/', views.book_view),
    path('books/<int:id>/', views.book_detail_view),
    path('add_book/', views.add_book_view),
    path('books/<int:id>/update/', views.update_book_view),
    path('books/<int:id>/delete/', views.delete_book_view)
]