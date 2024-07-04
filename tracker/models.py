from django.db import models
from django.contrib.auth.models import User


class FaseUser(models.Model):
    fases_choices = (
        (1, "Criança"),
        (2, "Adolescente"),
        (3, "Adulto"),
        (4, "Idoso"),
    )

    fase = models.CharField(max_length=15, choices=fases_choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Food(models.Model):
    name = models.CharField(max_length=50)
    carbs = models.FloatField()
    protein = models.FloatField()
    fats = models.FloatField()
    calories = models.IntegerField()

    def __str__(self):
        return self.name


class Consumed(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user.username} | {self.food.name}"
