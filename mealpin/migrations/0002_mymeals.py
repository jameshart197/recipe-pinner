# Generated by Django 3.2.20 on 2023-07-14 20:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mealpin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyMeals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meals', models.ManyToManyField(to='mealpin.Meal')),
                ('user', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='my_meals', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'My Meal',
                'verbose_name_plural': 'My Meals',
            },
        ),
    ]