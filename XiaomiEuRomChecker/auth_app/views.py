from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import redirect, render
from django.contrib.auth import login, get_user_model
from django.urls import reverse_lazy
from django.views import generic as views

from XiaomiEuRomChecker.auth_app.forms import RegistrationForm, ProfileEditForm
from XiaomiEuRomChecker.core.models import AvailableDevicesModel


# Create your views here.
class RegisterUserView(views.CreateView):
    template_name = 'auth_app/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)

        return result

    def dispatch(self, request_method, *args, **kwargs):
        if request_method.user.is_authenticated:
            return redirect('index')
        return super().dispatch(request_method, *args, **kwargs)


class LoginUserView(LoginView):
    template_name = 'auth_app/login.html'
    form_class = AuthenticationForm

    def dispatch(self, request_method, *args, **kwargs):
        if request_method.user.is_authenticated:
            return redirect('index')
        return super().dispatch(request_method, *args, **kwargs)


class LogoutUserView(LogoutView):
    pass


UserModel = get_user_model()


class BaseProfileView(views.View):
    model = UserModel
    success_url = reverse_lazy('index')


class ProfileDetailsView(BaseProfileView, LoginRequiredMixin, views.DetailView):
    template_name = 'auth_app/profile.html'
    pk_url_kwarg = 'pk'


@login_required(login_url='login')
def profile_edit(request, pk):
    current_user = UserModel.objects.get(id=pk)
    form = ProfileEditForm(request.POST or None, instance=current_user)

    if form.is_valid():
        chosen_device = form.cleaned_data['change_preferred_device']
        current_user.preferred_device = chosen_device
        current_user.save()
        return redirect('profile_details', pk=pk)
    else:
        form.fields['preferred_device'].widget.attrs['disabled'] = True

    return render(request, 'auth_app/profile_edit.html', {'form': form})


class ProfileDeleteView(BaseProfileView, LoginRequiredMixin, views.DeleteView):
    template_name = 'auth_app/profile_delete.html'
    pk_url_kwarg = 'pk'
