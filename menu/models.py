from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=256, unique=True, db_index=True)



class MenuItem(models.Model):
    name = models.CharField(max_length=256)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

