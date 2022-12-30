from django import template

from menu import models


register = template.Library()


@register.inclusion_tag("show_menu.html", name="draw")
def show_menu(name):
    menu = models.Menu.objects.get(name=name)
    try:
        resp = {}
        items = models.MenuItem.objects.filter(menu=menu)
        print(items)
        resp['menu'] = items
        return resp
    except models.Menu.DoesNotExist:
        raise template.TemplateSyntaxError("This menu is not found")