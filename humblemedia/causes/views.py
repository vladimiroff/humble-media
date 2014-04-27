from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.db.models import Sum
from django.views.generic import (CreateView, DeleteView, DetailView,
                                  ListView, UpdateView, FormView)

from humblemedia.utils import LoginRequiredMixin
from payments.models import Payment
from .models import Cause
from .forms import CauseForm


class CauseList(ListView):
    model = Cause
    context_object_name = 'causes'

    def get_queryset(self):
        return self.model.objects.filter(is_published=True, is_verified=True)


class MyCauseList(LoginRequiredMixin, CauseList):

    def get_queryset(self):
        return super().get_queryset().filter(creator=self.request.user)


class CauseDetails(DetailView):
    context_object_name = 'cause'
    model = Cause

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        amount = Payment.objects.filter(
            cause=context['cause']
        ).aggregate(paid=Sum('amount'))['paid']
        context['has_so_far'] = '{:.2f}'.format(0 if amount is None else amount)
        return context


class CauseUpdate(LoginRequiredMixin, UpdateView):
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


class SwitchPublishedCause(LoginRequiredMixin, FormView):

    def post(self, request, pk, **kwargs):
        obj = get_object_or_404(Cause, pk=pk, creator=request.user)
        obj.is_published = not obj.is_published
        return HttpResponseRedirect("")


class CauseDelete(LoginRequiredMixin, DeleteView):
    model = Cause
    success_url = reverse_lazy("causes:list")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.creator != self.request.user:
            raise HttpResponseForbidden("You cannot delete this cause")
        return obj


class CauseCreate(LoginRequiredMixin, CreateView):
    model = Cause
    form_class = CauseForm

    def get_success_url(self):
        return self.object.get_absolute_url()

    def form_valid(self, form):
        form.instance.creator = User.objects.get(pk=self.request.user.pk)
        return super().form_valid(form)
