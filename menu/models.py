from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=256, unique=True, db_index=True)

    def __str__(self) -> str:
        return self.name



class MenuItem(models.Model):
    name = models.CharField(max_length=256)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.name
