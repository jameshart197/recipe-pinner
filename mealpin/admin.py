from django.contrib import admin
from .models import Meal
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('recipe')


admin.site.register(Meal)
