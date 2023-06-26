from django.http import HttpResponse
from django.shortcuts import render
from .get_info_from_sourceforge import output


def index(request):
    return HttpResponse(output)
