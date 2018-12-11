from django.shortcuts import render
from station.models import Cs, UserCs


def index(request):
    css = Cs.objects.all()
    return render(request, 'ListCS.html', {"css": css})


def show_focus_station(request):
    user_css = UserCs.objects.filter(userTel=request.session['userTel'])
    return render(request, 'ListCS.html', {"user_css": user_css})

