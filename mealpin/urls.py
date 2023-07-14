from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create_meal, name='create_meal'),
    path('edit/<int:meal_id>', views.edit_meal, name='edit_meal'),
    path('delete/<int:meal_id>', views.delete_meal, name='delete_meal'),
]
