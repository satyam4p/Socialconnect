from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from .import forms
from django.views.generic import CreateView


# Create your views here.

class signup(CreateView):
    form_class = forms.usercreateform
    success_url=reverse_lazy("login")#reverse_lazy does not allows to redirect to login page untill user clicks submit button
    template_name = "basicapp/signup.html"

