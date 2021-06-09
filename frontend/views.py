from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView, DeleteView
from users.forms import CustomUserCreationForm, CustomUserUpdateForm
from users.models import CustomUser


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class HomePageView(TemplateView):
    template_name = 'home.html'


class ProfileView(TemplateView):
    model = CustomUser
    context_object_name = 'photo'
    template_name = 'profile.html'


class ProfileChangeView(UpdateView):
    form_class = CustomUserUpdateForm
    template_name = 'profilechange.html'

    def get_object(self, queryset=None):
        '''This method will load the object
           that will be used to load the form
           that will be edited'''
        return self.request.user

    def get_success_url(self, **kwargs):
        return reverse_lazy("profile", args=(self.object.id,))


class ProfileDeleteView(DeleteView):
    model = CustomUser
    success_url = reverse_lazy('home')
    template_name = 'profiledelete.html'
