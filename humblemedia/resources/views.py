from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.http.response import HttpResponseForbidden
from django.views.generic import (CreateView, DeleteView, DetailView,
                                  ListView, UpdateView, FormView)
from django.shortcuts import render, redirect, get_object_or_404

from humblemedia.utils import LoginRequiredMixin
from .models import Resource
from .forms import AttachmentForm, StripeForm


PUBLIC_FIELDS = (
    'title',
    'description',
    'min_price',
    'is_published',
)


class ResourceList(ListView):
    model = Resource
    template_name = 'resources/list.html'
    context_object_name = 'resources'

    def get_queryset(self):
        return self.model.objects.filter(is_published=True, is_verified=True)


class MyResourceList(ListView):
    model = Resource
    template_name = 'resources/list.html'
    context_object_name = 'resources'

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user,
                                         is_published=True,
                                         is_verified=True)


class ResourceDetail(DetailView):
    template_name = 'resources/detail.html'
    model = Resource


class ResourceCreate(LoginRequiredMixin, CreateView):
    model = Resource
    fields = PUBLIC_FIELDS
    template_name = 'resources/form.html'

    def get_success_url(self):
        return self.object.get_absolute_url()

    def form_valid(self, form):
        form.instance.author = User.objects.get(pk=self.request.user.pk)
        return super().form_valid(form)


class ResourceEdit(LoginRequiredMixin, UpdateView):
    model = Resource
    fields = PUBLIC_FIELDS
    template_name = 'resources/edit.html'

    def get_object(self, queryset=None):
        resource = super().get_object(queryset)
        if not resource.author == self.request.user:
            raise HttpResponseForbidden("You cannot delete this resource")
        return resource

    def get_success_url(self):
        return self.object.get_absolute_url()


class ResourceDelete(LoginRequiredMixin, DeleteView):
    model = Resource
    success_url = reverse_lazy('resources:list')

    def get_object(self, queryset=None):
        resource = super().get_object(queryset)
        if not resource.author == self.request.user:
            raise HttpResponseForbidden("You cannot delete this resource")
        return resource


class ResourceBuy(LoginRequiredMixin, FormView):
    template_name = 'resources/payment.html'

    def form_valid(self, form):
        form.charge()

    def get(self, request, pk, **kwargs):
        resource = get_object_or_404(Resource, pk=pk)
        form = StripeForm(request.user, resource)
        return self.render_to_response(self.get_context_data(form=form, resource=resource))

    def post(self, request, pk, **kwargs):
        resource = get_object_or_404(Resource, pk=pk)
        form = StripeForm(request.user, resource)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


def upload_attachment(request, model, pk):
    data = request.POST if request.POST else None
    files = request.FILES
    form = AttachmentForm(data, files, model=model, id=pk)
    if form.is_valid():
        form.save()
        return redirect('/{}/{}/'.format(model, pk))
    return render(request, 'resources/upload.html', locals())

