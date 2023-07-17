from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('adminpanel', views.admin_view, name="admin_panel"),
    path('mymeals', views.my_meals, name="my_meals"),
    path('create', views.create_meal, name='create_meal'),
    path('edit/<int:meal_id>', views.edit_meal, name='edit_meal'),
    path('delete/<int:meal_id>', views.delete_meal, name='delete_meal'),
    path('pin/<int:meal_id>', views.add_meal_to_plan, name='user_pin'),
    path('unpin/<int:meal_id>', views.remove_meal_from_plan, name='user_unpin'),
    path('info/dialog/<int:meal_id>', views.info_dialog, name='info_dialog'),
]
