from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Meal, MyMeals
from .forms import MealForm


def index(request):
    if request.user.is_authenticated:
        meal_plan = MyMeals.objects.get_or_create(user=request.user)
        # if meal_plan is None:
        #     meal_plan = MyMeals.objects.create(
        #         user=request.user
        #     )
        context = {"meals": Meal.objects.all()}
        return render(request, "home.html", context)
    else:
        return render(request, "index.html")


# Admin Panel


@login_required
def admin_view(request):
    if not request.user.is_staff:
        messages.error(request, f"Not eligible for this action")

        return redirect(reverse("index"))
    context = {"meals": Meal.objects.all()}

    return render(request, "admin_view.html", context)


# Create Meal


@login_required
def create_meal(request):
    if not request.user.is_staff:
        messages.error(request, f"Not eligible for this action")

        return redirect(reverse("index"))

    if request.method == "POST":
        form = MealForm(request.POST, request.FILES)

        if form.is_valid():
            meal_name = request.POST["title"]
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
            meal_name = request.POST["title"]
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

# Add


@login_required
def add_meal_to_plan(request, meal_id):
    meal = get_object_or_404(Meal, id=meal_id)
    if meal:
        user_meal_list, created = MyMeals.objects.get_or_create(user=request.user)
        user_meal_list.meals.add(meal)
        messages.success(request, f"{meal.title} succesfully added")

    return redirect(reverse("index"))

# Remove


@login_required
def remove_meal_from_plan(request, meal_id):
    meal = get_object_or_404(Meal, id=meal_id)
    if meal:
        user_meal_list, created = MyMeals.objects.get_or_create(user=request.user)
        user_meal_list.meals.remove(meal)
        messages.success(request, f"{meal.title} succesfully removed")

    return redirect(reverse("index"))
