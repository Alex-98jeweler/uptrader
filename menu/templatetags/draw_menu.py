from django import template

from menu import models


register = template.Library()


@register.inclusion_tag("show_menu.html", name="draw")
def show_menu(name):
    menu = models.Menu.objects.get(name=name)
    try:
        resp = {"menu": []}
        items = models.MenuItem.objects.filter(menu=menu).filter(parent=None)
        for item in items:
            children = models.MenuItem.objects.filter(parent=item)
            flag = False
            if children:
                flag = True
            resp["menu"].append({
                "name": item.name,
                'children': children,
                'has_children': flag

            })
        return resp
    except models.Menu.DoesNotExist:
        raise template.TemplateSyntaxError("This menu is not found")