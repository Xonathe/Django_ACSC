from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from web_cp.connector import Connector

status = 1  # Статус кнопок: 0 > Запущено \ 1 > Остановлено
acsc = Connector()


def main(request):
    global status
    if request.POST.get('START'):
        print("status = " + str(status))
        status = 0
        acsc.run()
    elif request.POST.get('STOP'):
        status = 1
        acsc.wait()
    if request.POST.get('AUTH'):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return render(request, 'web_cp/profile.html', {'status': status})
        else:
            return render(request, 'web_cp/login.html', {'form': form})
    else:
        form = LoginForm()
    if request.user.is_authenticated:
        return render(request, 'web_cp/profile.html', {'status': status})
    else:
        return render(request, 'web_cp/login.html', {'form': form})


@login_required(redirect_field_name=None)
def profile():
    return HttpResponseRedirect(reverse('profile'))


@login_required(redirect_field_name=None)
def add_data(request):
    if request.POST:
        _name = request.POST.get('select')  # ФИО
        _change = request.POST['radio']  # 1 - текущее время, 2 - конкретное время
        _time = request.POST.get('frm_dt')  # время, "" или None
        try:
            _time = datetime.fromisoformat(_time).strftime('%d.%m.%Y %H:%M:%S')
        except ValueError:
            pass
        except TypeError:
            pass
        print(_name, _change, _time)
        return HttpResponseRedirect(reverse('logs'))
    return render(request, 'web_cp/add_data.html')


@login_required(redirect_field_name=None)
def logs(request):
    return render(request, 'web_cp/logs.html')


def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def page_not_found_view(request, exception):
    return redirect(request.GET.get('next', 'login'))
