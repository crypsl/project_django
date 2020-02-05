from django.urls import path
from .views import HomeView, add_publication, add_book, edit_book

app_name = 'app'

urlpatterns = [
    path('home/',HomeView.as_view(), name='home'),
    path('addpublication/', add_publication, name='add_publication'),
    path('addbook/',add_book, name='add_book'),
    path('editbook/<int:book_id>/',edit_book, name='edit_book')
]
