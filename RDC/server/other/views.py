from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def all(request):
    ctx = {
        "file_names": [i+1 for i in range(9)]
    }
    return render(request, "other/all.html", ctx)