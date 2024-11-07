from django.urls import path
from . import views
urlpatterns = [
    path('addbook',views.add_book,name='addbook'),
    path('display', views.display_books,name='display'),
    path('edit<pk>',views.edit, name='edit'),
    path('delete<pk>',views.delete, name="delete"),
    path('', views.homepage)
]