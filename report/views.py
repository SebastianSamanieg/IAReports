from django.shortcuts import render


def index (request):
    return render ("report/index.html", context={})