from django.contrib import admin
from .models import Meal, MyMeals
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Meal)
class MealAdmin(SummernoteModelAdmin):

    summernote_fields = ('recipe')


admin.site.register(MyMeals)
