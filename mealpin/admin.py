from django.contrib import admin
from .models import Meal
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Meal)
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('recipe')
