from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from XiaomiEuRomChecker.links.models import LinksModel

UserModel = get_user_model()


@login_required
def link_details(request, slug):
    link = LinksModel.objects.get(slug=slug)
    return render(request, 'links/link_details.html', {'link': link})


class LinkCreateView(LoginRequiredMixin, CreateView):
    model = LinksModel
    template_name = 'links/link_create.html'
    fields = ['link_name', 'link_url', 'short_link', 'link_description']


class LinkEditView(LoginRequiredMixin, UpdateView):
    pass


class LinkDeleteView(DeleteView):
    pass
