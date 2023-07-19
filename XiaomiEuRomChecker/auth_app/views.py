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
from XiaomiEuRomChecker.links.models import LinksModel


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


@login_required(login_url='login')
def profile_details(request, pk):
    current_user = UserModel.objects.get(pk=pk)
    links = LinksModel.objects.filter(user_id=pk).all()
    context = {
        "user": current_user,
        'links': links
    }
    return render(request, 'auth_app/profile.html', context)


@login_required(login_url='login')
def profile_edit(request, pk):
    current_user = UserModel.objects.get(pk=pk)
    form = ProfileEditForm(request.POST or None, instance=current_user)

    if form.is_valid():
        instance = form.save(commit=False)
        chosen_device = form.cleaned_data['change_preferred_device']
        if not chosen_device:
            chosen_device = "No Device"
        instance.preferred_device = chosen_device
        instance.save()
        return redirect('profile_details', pk=pk)
    else:
        form.fields['preferred_device'].widget.attrs['disabled'] = True

    return render(request, 'auth_app/profile_edit.html', {'form': form})


class ProfileDeleteView(LoginRequiredMixin, views.DeleteView):
    model = UserModel
    template_name = 'auth_app/profile_delete.html'
    pk_url_kwarg = 'pk'


@login_required(login_url='login')
def my_device(request, pk):
    user = UserModel.objects.get(pk=request.user.id)
    user_device = user.preferred_device
    if user_device == "No Device":
        return redirect('index')
    else:
        chosen_device = AvailableDevicesModel.objects.get(market_name=user_device)
        return render(request, 'device_info.html', {'chosen_device': chosen_device})
