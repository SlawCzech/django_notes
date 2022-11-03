from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render, redirect, reverse
from django.template import loader
from django.contrib import messages
from django.contrib.auth import login

from .forms import NameForm, UserForm, UserDetailForm


def home(request):
    template = loader.get_template('coffeeshop/home.html')
    context = {}
    return HttpResponse(template.render(context, request))


def thanks(request):
    return render(request, 'coffeeshop/thanks.html')


# def signup(request):
#     if request.method == 'POST':
#         form = NameForm(request.POST)
#
#         if form.is_valid():   # to jest trigger odpalający walidatory, zwraca True lub False
#             form.save()
#             messages.add_message(request, messages.SUCCESS, f'it works properly, {form.cleaned_data.get("name")}')
#             return HttpResponseRedirect('/thanks')
#
#     else:
#         form = NameForm()
#
#     template = loader.get_template('coffeeshop/signup.html')
#     context = {'form': form}
#     return HttpResponse(template.render(context, request))


def signup(request):
    form = UserForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.add_message(request, messages.SUCCESS, 'It works better now!')
            return redirect(reverse('coffeeshop:details'))
    return render(request, 'coffeeshop/signup.html', {'form': form})


def details(request):
    if request.method == 'POST':
        form = UserDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('coffeeshop:thanks'))
    else:
        form = UserDetailForm(initial={'username': request.user.username, 'email': request.user.email})

    return render(request, 'coffeeshop/signup.html', {'form': form})


