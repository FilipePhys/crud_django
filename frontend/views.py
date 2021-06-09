from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView
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

    # def form_valid(self, form):
    #     ctx = {}
    #     print(form)
    #     if form.is_valid():
    #         form.save(commit=False)
    #         updateuser = CustomUser(**form.cleaned_data)
    #         updateuser.save()
    #         print(form)
    #         ctx['confirm_added'] = f"Segura na minha mão {form.cleaned_data['username']}, otário."
    #     else:
    #         ctx['errors'] = form.errors
    #
    #     return render(request=request, template_name='profilechange.html', context=ctx)



#
# TIO PABLO FEZ COMIGO
# def test_view(request):
#     ctx = {}
#     if request.method == 'POST':
#         form = CustomUserForm(data=request.POST)
#         print(form)
#         if form.is_valid():
#             form.save()
#             #newuser = CustomUser(**form.cleaned_data)
#             #newuser.save()
#             ctx['confirm_added'] = f"Segura na minha mão {form.cleaned_data['username']}, otário."
#         else:
#             ctx['errors'] = form.errors
#
#         # newuser.username = request.POST['name']
#         # newuser.birth_date = request.POST['age']
#         # newuser.email = request.POST['email']
#         # newuser.tiopablo = request.POST['name']
#         # newuser.save()
#         # ctx['confirm_added'] = f"Segura na minha mão {request.POST['name']}, otário"
#
#
#     return render(request=request, template_name='teste.html', context=ctx)

