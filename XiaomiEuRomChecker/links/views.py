from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from XiaomiEuRomChecker.links.forms import SaveLinkForm, EditLinkForm
from XiaomiEuRomChecker.links.functionality import shorten_url
from XiaomiEuRomChecker.links.models import LinksModel

UserModel = get_user_model()


class LinkDetailsView(LoginRequiredMixin, DetailView):
    model = LinksModel
    template_name = 'links/link_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['link'] = LinksModel.objects.get(slug=self.kwargs[self.slug_url_kwarg])
        return context

    def get_success_url(self):
        return reverse('link_details', kwargs={'user_id': self.kwargs['user_id'], 'slug': self.kwargs['slug']})


class LinkCreateView(LoginRequiredMixin, CreateView):
    model = LinksModel
    template_name = 'links/link_create.html'
    form_class = SaveLinkForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.link_url = self.request.session['uid']
        del self.request.session['uid']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('my_links', kwargs={'user_id': self.request.user.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['links'] = LinksModel.objects.filter(user=self.request.user).order_by('-created_at').all()
        return context


class LinkEditView(LoginRequiredMixin, UpdateView):
    model = LinksModel
    template_name = 'links/link_edit.html'
    form_class = EditLinkForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['link'] = LinksModel.objects.get(slug=self.kwargs[self.slug_url_kwarg])
        return context

    def get_success_url(self):
        return reverse('link_details', kwargs={'user_id': self.kwargs['user_id'], 'slug': self.kwargs['slug']})


class LinkDeleteView(LoginRequiredMixin, DeleteView):
    model = LinksModel
    template_name = 'links/link_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['link'] = LinksModel.objects.get(slug=self.kwargs[self.slug_url_kwarg])
        return context

    def get_success_url(self):
        return reverse('my_links', kwargs={'user_id': self.kwargs['user_id']})


class MyLinksView(LoginRequiredMixin, ListView):
    model = LinksModel
    template_name = 'links/my_links.html'

    def get_success_url(self):
        return reverse('my_links', kwargs={'user_id': self.request.user.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['links'] = LinksModel.objects.filter(user=self.request.user).order_by('-created_at').all()
        return context


@login_required
def create_short_link(request, user_id, slug):
    link = LinksModel.objects.get(slug=slug)

    try:
        link.short_link = shorten_url(link.link_url)
        link.save()

    # Will raise if the link doesn't start with the needed from bit.ly prefix (https:// or http://)
    except:
        return redirect('index')

    return redirect("link_details", user_id=request.user.id, slug=link.slug)
