FROM python:3

ENV PYTHONDONTWRITEBYDECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY manage.py /app/manage.py
#COPY certbot /app/certbot
COPY nginx /app/nginx
COPY templates /app/templates
COPY XiaomiEuRomChecker /app/XiaomiEuRomChecker
COPY xiaomi.eu_rom_checker_db /app/xiaomi.eu_rom_checker_db