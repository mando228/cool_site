from django import template

from Cool_Site.models import *

# ---------------------------
register = template.Library()
# ---------------------------


@register.inclusion_tag('category_list.html')
def show_catigory_box():
    cats = Card_Category.objects.all()
    return {"cats" : cats}

# cats встречается несколько раз и чтобы не нарушать принцип <не повторяйся>
# мы его написали один раз вот в этой функции | в дальнейшем категории можно по разному кастомизировать
# с помощью фильтров