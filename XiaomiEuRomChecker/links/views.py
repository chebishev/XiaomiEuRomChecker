from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import request
from django.shortcuts import render, get_object_or_404
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
        return reverse('links:link_details', kwargs={'user_id': self.kwargs['user_id'], 'slug': self.kwargs['slug']})

# TODO To be deleted
# @login_required
# def link_details(request, slug):
#     link = LinksModel.objects.get(slug=slug)
#     return render(request, 'links/link_details.html', {'link': link})


class LinkCreateView(LoginRequiredMixin, CreateView):
    model = LinksModel
    template_name = 'links/link_create.html'
    fields = ['link_name', 'link_url', 'link_description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class LinkEditView(LoginRequiredMixin, UpdateView):
    pass


class LinkDeleteView(DeleteView):
    pass
