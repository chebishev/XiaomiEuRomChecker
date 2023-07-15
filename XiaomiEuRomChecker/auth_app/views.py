from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views, login
from django.contrib.auth import forms as auth_forms
from django.urls import reverse_lazy
from django.views import generic as views


# Create your views here.
class RegisterUserView(views.CreateView):
    template_name = 'auth_app/register.html'
    form_class = auth_forms.UserCreationForm
    success_url = reverse_lazy('register')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)

        return result


class LoginUserView(LoginView):
    template_name = 'auth_app/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.request.GET.get('next', reverse_lazy('index')))
        return super().dispatch(request, *args, **kwargs)

class LogoutUserView(LogoutView):
    redirect_url = reverse_lazy('index')

