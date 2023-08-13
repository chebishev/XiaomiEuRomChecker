from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import redirect, render
from django.contrib.auth import login, get_user_model
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView
from XiaomiEuRomChecker.auth_app.forms import ProfileEditForm, RegisterUserForm, LoginUserForm
from XiaomiEuRomChecker.core.models import AvailableDevicesModel
from XiaomiEuRomChecker.links.models import LinksModel

UserModel = get_user_model()


# Create your views here.
class RegisterUserView(CreateView):
    template_name = 'auth_app/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('index')

    # autologin after registration
    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)

        return result

    # in order to prevent logged users to access register page:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)

    # return to the previous page after login
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['next'] = self.request.GET.get('next', '')

        return context

    def get_success_url(self):
        return self.request.POST.get('next', self.success_url)


class LoginUserView(LoginView):
    template_name = 'auth_app/login.html'
    form_class = LoginUserForm

    def dispatch(self, request_method, *args, **kwargs):
        if request_method.user.is_authenticated:
            return redirect('index')
        return super().dispatch(request_method, *args, **kwargs)


class LogoutUserView(LogoutView):
    pass


@login_required
def profile_details(request, pk):
    links_to_show = 5
    current_user = UserModel.objects.get(pk=pk)

    # Check if the logged-in user matches the requested user's profile or has appropriate permissions.
    if request.user != current_user:
        # You can customize the error message or response as needed.
        return redirect('index')

    links = LinksModel.objects.filter(user_id=pk).order_by('-updated_at').all()[:links_to_show]
    context = {
        "user": current_user,
        'links': links,
        'links_to_show': links_to_show
    }
    return render(request, 'auth_app/profile.html', context)


@login_required
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


class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = UserModel
    template_name = 'auth_app/profile_delete.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('index')


@login_required
def my_device(request, pk):
    user = UserModel.objects.get(pk=request.user.id)
    user_device = user.preferred_device
    if user_device == "No Device":
        return redirect('index')
    else:
        chosen_device = AvailableDevicesModel.objects.get(market_name=user_device)
        return render(request, 'core/device_info.html', {'chosen_device': chosen_device})
