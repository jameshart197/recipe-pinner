from django.db import models
from django.contrib.auth.models import User


class Meal(models.Model):
    MEAL_TYPE = ((0, "Breakfast"), (1, "Lunch"), (2, "Dinner"), (3, "Dessert"), (4, "Snack"))
    title = models.CharField(max_length=200, unique=True)
    meal_type = models.IntegerField(choices=MEAL_TYPE, default=0)
    preptime_in_minutes = models.DecimalField(max_digits=3, decimal_places=1)
    calories_in_grams = models.DecimalField(max_digits=5, decimal_places=1)
    protein_in_grams = models.DecimalField(max_digits=4, decimal_places=1)
    fat_in_grams = models.DecimalField(max_digits=4, decimal_places=1)
    carbs_in_grams = models.DecimalField(max_digits=4, decimal_places=1)
    recipe = models.TextField(default="This recipe has not been added yet!")

    def __str__(self):
        return f'{self.title} - {self.preptime_in_minutes} minutes to prep - {self.calories_in_grams} Kcal'


class MyMeals(models.Model):
    user = models.OneToOneField(User, related_name='my_meals', on_delete=models.CASCADE, default=1)
    meals = models.ManyToManyField(Meal)
    
    class Meta:
        verbose_name = 'My Meal'
        verbose_name_plural = 'My Meals'

    def __str__(self):
        return f'{self.user.username} - {self.meals.count()}'
