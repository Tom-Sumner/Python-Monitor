from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import EmailAccount

# Create your views here.
@login_required
def all(request):
    ctx = {
        "accounts": EmailAccount.objects.all(),
        "title": "All Accounts"
        }
    return render(request, "accounts/all.html", context=ctx)