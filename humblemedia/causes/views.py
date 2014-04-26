from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.http.response import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from .models import Cause
from .forms import CauseForm


class OwnedViewMixin:
    pass


class AuthViewMixin:

    @classmethod
    def as_view(cls, *args, **kwargs):
        res = super().as_view(*args, **kwargs)
        return login_required(res)


class CauseList(ListView):
    model = Cause

    def get_queryset(self):
        return self.model.objects.filter(is_published=True, is_verified=True)


class MyCauseList(AuthViewMixin, CauseList):

    def get_queryset(self):
        return super().get_queryset().filter(creator=self.request.user)

class CauseDetails(DetailView):
    model = Cause

class CauseUpdate(AuthViewMixin, UpdateView):
    model = Cause
    form_class = CauseForm

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.creator != self.request.user:
            raise HttpResponseForbidden("You cannot update this cause")
        return obj

    def form_valid(self, form):
        form.instance.is_verified = False
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.get_absolute_url()

class SwitchPublishedCause(AuthViewMixin, FormView):

    def post(self, request, pk, **kwargs):
        obj = get_object_or_404(Cause, pk=pk, creator=request.user)
        obj.is_published = not obj.is_published
        return HttpResponseRedirect("")

class CauseDelete(AuthViewMixin, DeleteView):
    model = Cause
    success_url = reverse_lazy("cause_list")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.creator != self.request.user:
            raise HttpResponseForbidden("You cannot delete this cause")
        return obj

class CauseCreate(AuthViewMixin, CreateView):
    model = Cause
    form_class = CauseForm

    def get_success_url(self):
        return self.object.get_absolute_url()

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
