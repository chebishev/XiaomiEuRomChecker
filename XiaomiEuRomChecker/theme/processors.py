import random

from XiaomiEuRomChecker.theme.models import ThemeModel, TipOfTheDayModel


def theme_colors(request):
    color = ThemeModel.objects.first()
    return {'color': color}


def tip_of_the_day(request):
    start = 1
    stop = len(TipOfTheDayModel.objects.all())
    tip_to_show = TipOfTheDayModel.objects.get(id=random.randint(start, stop))
    return {'tip': tip_to_show}
