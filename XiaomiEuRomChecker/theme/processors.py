import random
import json


def theme_colors(request):
    # change the file to default_theme.json to load default colors
    with open("XiaomiEuRomChecker/theme/custom_theme.json", "r", encoding="utf-8") as theme_file:
        colors = json.load(theme_file)
    return {'color': colors}


def tip_of_the_day(request):
    with open("XiaomiEuRomChecker/theme/tips.json", "r", encoding="utf-8") as tips_file:
        all_tips = json.load(tips_file)
        # get a random tip
        start = 0
        stop = len(all_tips) - 1
        index = random.randint(start, stop)
        tip_to_show = all_tips[index]
        print(index)
        return {'tip': tip_to_show}

