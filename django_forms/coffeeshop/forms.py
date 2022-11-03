from django import forms
from . import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, reverse


class NameForm(forms.Form):
    name = forms.CharField(label='Your name', min_length=3, max_length=100)   # input type text

    def save(self):
        pass


class UserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'email')
        # fields = '__all__'  nie używa się!
        # exclude = ('email', )    też się nie używa

    def save(self, commit=True):
        m = super().save(commit=False)
        m.password = make_password(self.cleaned_data.get('password'))
        m.username = self.cleaned_data.get('username').lower()

        if commit:
            m.save()
        return m


class UserDetailForm(forms.ModelForm):

    class Meta:
        model = models.UserDetail
        fields = '__all__'


