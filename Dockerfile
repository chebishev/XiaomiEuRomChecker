FROM python:3

ENV PYTHONDONTWRITEBYDECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /XiaomiEuRomChecker

COPY requirements.txt /XiaomiEuRomChecker/

RUN pip install -r requirements.txt

COPY . /XiaomiEuRomChecker/