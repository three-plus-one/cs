from django.shortcuts import render
from station.models import Cs


def index(request):
    cs_add_state = CsAddState()
    cs_add_state.__init__()
    css = Cs.objects.all()
    return render(request, 'ListCS.html', {"css": css, "csAddState": cs_add_state})


def show_common(request, cs_add=None):
    cs_add_state = CsAddState()
    cs_add_state.state = 1
    cs_add_state.cs_add = cs_add
    if cs_add is not None:
        css = Cs.objects.filter(csAdd="精思苑"+cs_add.__str__()+"号楼")
    else:
        css = Cs.objects.all()
    print("*********show_common*******")
    return render(request, 'ListCS.html', {"css": css, "csAddState": cs_add_state})


def show_free(request, cs_add=None):
    cs_add_state = CsAddState()
    cs_add_state.state = 2
    cs_add_state.cs_add = cs_add
    css = Cs.objects.all()
    print("*********show_free*******")
    return render(request, 'ListCS.html', {"css": css, "csAddState": cs_add_state})


def show_focus(request, cs_add=None):
    cs_add_state = CsAddState()
    cs_add_state.state = 3
    cs_add_state.cs_add = cs_add
    css = Cs.objects.all()
    print("*********show_focus*******")
    return render(request, 'ListCS.html', {"css": css, "csAddState": cs_add_state})


class CsAddState(object):
    def __init__(self):
        self.state = 1
        self.cs_add = 1
