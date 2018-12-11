from django.http import HttpResponseRedirect
from django.shortcuts import render
from login.forms import UserForm
from login.models import Users


def login(request):
    return render(request, 'login.html')


def login_action(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            tel = uf.cleaned_data['inputTel']
            pwd = uf.cleaned_data['inputPassword']
            user = Users.objects.filter(userTel=tel, userPwd=pwd)
            if user:
                response = HttpResponseRedirect('/index/')
                response.set_cookie('user', tel, 3600)
                session_user = Users.objects.get(userTel=tel)
                request.session['userTel'] = session_user.userTel
                request.session['userName'] = session_user.userName
                request.session['userMail'] = session_user.userMail
                return HttpResponseRedirect('/index/')
            else:
                return render(request, 'login.html')
    else:
        return render(request, 'login.html')

