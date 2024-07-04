from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from .models import *
from django.template.defaultfilters import floatformat
from django.contrib.auth.models import User
from django.db.models import Sum


@login_required(login_url=reverse_lazy("login"))
def trackerAuth(request):
    if FaseUser.objects.filter(user=request.user).exists():
        return redirect("tracker")
    else:
        if request.method == "GET":
            return render(request, "tracker/auth.html")
        else:
            fase = request.POST["fases"]
            FaseUser.objects.create(
                fase=fase,
                user=request.user,
            ).save()

            return redirect(reverse("tracker"))


@login_required(login_url=reverse_lazy("login"))
def tracker(request):
    foods = Food.objects.all()
    consumed = Consumed.objects.filter(user=request.user)
    if request.method == "GET":
        tot_carbs = consumed.aggregate(Sum("food__carbs"))["food__carbs__sum"] or 0
        tot_prots = consumed.aggregate(Sum("food__protein"))["food__protein__sum"] or 0
        tot_fats = consumed.aggregate(Sum("food__fats"))["food__fats__sum"] or 0
        tot_cals = consumed.aggregate(Sum("food__calories"))["food__calories__sum"] or 0

        # Formata os totais para exibição
        tot_carbs_formatted = float(floatformat(tot_carbs, 2))
        tot_prots_formatted = float(floatformat(tot_prots, 2))
        tot_fats_formatted = float(floatformat(tot_fats, 2))
        tot_cals_formatted = float(floatformat(tot_cals, 0))
        percentage = tot_cals/25
        tot_all = tot_carbs_formatted + tot_fats_formatted + tot_prots_formatted or 1 
        carbsP = float(floatformat((tot_carbs_formatted * 100)/tot_all, 2))
        protsP = float(floatformat((tot_prots_formatted * 100)/tot_all, 2))
        fatsP = float(floatformat((tot_fats_formatted * 100)/tot_all, 2)) 
        return render(
            request,
            "tracker/tracker.html",
            {
                "foods": foods,
                "consumed": consumed,
                "tot_carbs": tot_carbs_formatted,
                "tot_prots": tot_prots_formatted,
                "tot_fats": tot_fats_formatted,
                "tot_cals": tot_cals_formatted,
                "percentage": percentage,
                "carbsP": carbsP,
                "protsP": protsP,
                "fatsP": fatsP,
            },
        )
    else:
        id = request.POST["slt"]
        Consumed.objects.create(
            food=Food.objects.get(id=id),
            user=request.user,
        ).save()

        return redirect(reverse("tracker"))


@login_required(login_url=reverse_lazy("login"))
def delete_consumed_food(request, id):
    Consumed.objects.get(id=id).delete()
    return redirect(reverse("tracker"))
