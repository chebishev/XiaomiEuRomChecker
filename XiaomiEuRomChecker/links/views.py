from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
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
    fields = ['link_name']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.link_url = self.request.session['uid']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('profile_details', kwargs={
            "user_id": self.request.user.id
        })


class LinkEditView(LoginRequiredMixin, UpdateView):
    model = LinksModel
    template_name = 'links/link_edit.html'
    fields = ['link_name', 'link_description']

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
        return reverse('link_details', kwargs={'user_id': self.kwargs['user_id'], 'slug': self.kwargs['slug']})
