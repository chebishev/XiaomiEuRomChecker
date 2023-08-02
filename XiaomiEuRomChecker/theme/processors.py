import random

from XiaomiEuRomChecker.theme.models import ThemeModel, TipOfTheDayModel


def theme_colors(request):
    color = ThemeModel.objects.first()
    return {'color': color}


def tip_of_the_day(request):
    # get a random tip if any tips in the db
    try:
        all_tips = TipOfTheDayModel.objects.all()
        start = 1
        stop = len(all_tips)
        tip_to_show = TipOfTheDayModel.objects.get(id=random.randint(start, stop))
        return {'tip': tip_to_show}
    
    # if there is nothing in the database send None to the context
    except TipOfTheDayModel.DoesNotExist:
        return {'tip': None}

