from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Meal
from .forms import MealForm


def index(request):
    return render(request, "index.html")


# Admin Panel

@login_required
def meal_list(request):
    if not request.user.is_staff:
        messages.error(request, f"Not eligible for this action")

        return redirect(reverse("index"))
    context = {
      'meals': Meal.objects.all()
    }

    return render(request, 'admin_view.html', context)

# Create Meal


@login_required
def create_meal(request):
    if not request.user.is_staff:
        messages.error(request, f"Not eligible for this action")

        return redirect(reverse("index"))

    if request.method == "POST":
        form = MealForm(request.POST, request.FILES)

        if form.is_valid():
            meal_name = request.POST['title']
            form.save()
            messages.success(request, f"{meal_name} added to list")

        else:
            messages.error(request, f"No Meal added to the list")

        return redirect(reverse("index"))
    form = MealForm()
    return render(request, "create_meal.html", {"form": form})


# Edit Meal


@login_required
def edit_meal(request, meal_id):
    if not request.user.is_staff:
        messages.error(request, f"Not eligible for this action")

        return redirect(reverse("index"))

    meal = get_object_or_404(Meal, id=meal_id)

    if request.method == "POST":
        form = MealForm(request.POST, request.FILES, instance=meal)

        if form.is_valid():
            meal_name = request.POST['title']
            form.save()
            messages.success(request, f"{meal_name} succesfully edited")

        return redirect(reverse("index"))

    form = MealForm(instance=meal)

    return render(request, "edit_meal.html", {"form": form, "meal_id_context": meal_id})


# Delete Meal


@login_required
def delete_meal(request, meal_id): 
    if not request.user.is_staff:
        messages.error(request, f"Not eligible for this action")

        return redirect(reverse("index"))

    if request.method == "POST":
        meal = get_object_or_404(Meal, id=meal_id)  # or Meal.objects.all()
        meal_name = meal.title
        meal.delete()
        messages.success(request, f"{meal_name} succesfully deleted")

        return redirect(reverse("index"))
