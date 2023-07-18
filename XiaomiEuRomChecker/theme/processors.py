import random

from XiaomiEuRomChecker.theme.models import ThemeModel, TipOfTheDayModel


def theme_colors(request):
    color = ThemeModel.objects.first()
    return {'color': color}


def tip_of_the_day(request):
    all_tips = TipOfTheDayModel.objects.all()
    start = 1
    stop = len(all_tips)
    if all_tips:
        tip_to_show = TipOfTheDayModel.objects.get(id=random.randint(start, stop))
        return {'tip': tip_to_show}
    # if there is nothing in the database send None to the context
    return {'tip': None}
