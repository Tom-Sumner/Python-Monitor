from django.shortcuts import render
from .models import Computer
from django.contrib.auth.decorators import login_required

@login_required
def intro(request):
    return render(request, "computer/intro.html")

@login_required
def all(request):
    ctx = {
        "computers": Computer.objects.all(),
        "title": "All PC's"
        }
    return render(request, "computer/all.html", context=ctx)