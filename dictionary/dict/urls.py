from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_word/', views.addWord, name="add_word"),
    path('update_word/<str:pk>/', views.updateWord, name="update_word"),
    path('delete_word/<str:pk>/', views.deleteWord, name="delete_word"),
]
