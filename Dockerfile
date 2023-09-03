FROM python:3

ENV PYTHONDONTWRITEBYDECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /XiaomiEuRomChecker

COPY requirements.txt /XiaomiEuRomChecker/

RUN pip install -r requirements.txt

COPY manage.py /XiaomiEuRomChecker/manage.py
COPY certbot /XiaomiEuRomChecker/certbot
COPY nginx /XiaomiEuRomChecker/nginx
COPY static /XiaomiEuRomChecker/static
COPY templates /XiaomiEuRomChecker/templates
COPY XiaomiEuRomChecker /XiaomiEuRomChecker/XiaomiEuRomChecker
COPY xiaomi.eu_rom_checker_db /XiaomiEuRomChecker/xiaomi.eu_rom_checker_db