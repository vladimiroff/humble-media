from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http.response import HttpResponse, HttpResponseForbidden, HttpResponseNotFound
from django.views.generic import (CreateView, DeleteView, DetailView,
                                  ListView, UpdateView, FormView)
from django.shortcuts import render, redirect, get_object_or_404

from humblemedia.utils import LoginRequiredMixin
from .models import Resource, Attachment
from .forms import AttachmentForm, StripeForm
from .processing import MediaManager


PUBLIC_FIELDS = (
    'title',
    'description',
    'min_price',
    'causes',
    'license',
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


class ImageList(ListView):
    model = Resource
    template_name = 'resources/list.html'
    context_object_name = 'resources'

    def get_queryset(self):
        return self.model.images.all()

class AudioList(ListView):
    model = Resource
    template_name = 'resources/list.html'
    context_object_name = 'resources'

    def get_queryset(self):
        return self.model.audios.all()


class VideoList(ListView):
    model = Resource
    template_name = 'resources/list.html'
    context_object_name = 'resources'

    def get_queryset(self):
        return self.model.videos.all()


class DocumentList(ListView):
    model = Resource
    template_name = 'resources/list.html'
    context_object_name = 'resources'

    def get_queryset(self):
        return self.model.documents.all()


class ResourceDetail(DetailView):
    template_name = 'resources/detail.html'
    model = Resource

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_bought'] = context['resource'].is_bought_by(self.request.user)
        return context


class ResourceCreate(LoginRequiredMixin, CreateView):
    model = Resource
    fields = PUBLIC_FIELDS
    template_name = 'resources/form.html'

    def get_success_url(self):
        return reverse('upload-attachment', kwargs={'pk': self.resource.pk, 'model': "resources"})

    def form_valid(self, form):
        self.resource = form.instance
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
        return redirect('resources:download', pk=self.resource.pk)

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(form=form,
                                  resource=self.resource,
                                  stripe_secret=settings.STRIPE_API_PUBLIC_KEY))

    def get(self, request, pk, **kwargs):
        self.resource = get_object_or_404(Resource, pk=pk)
        form = StripeForm(request.user, self.resource, **self.get_form_kwargs())
        return self.render_to_response(
            self.get_context_data(form=form,
                                  resource=self.resource,
                                  stripe_secret=settings.STRIPE_API_PUBLIC_KEY))

    def post(self, request, pk, **kwargs):
        self.resource = get_object_or_404(Resource, pk=pk)
        form = StripeForm(request.user, self.resource, **self.get_form_kwargs())
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


@login_required
def upload_attachment(request, model, pk):
    obj = get_object_or_404(Resource, pk=pk)
    if request.user != obj.author:
        return HttpResponseForbidden("Cannot upload in resources you did not create")
    data = request.POST if request.POST else None
    files = request.FILES if request.POST else None
    form = AttachmentForm(data, files, model=model, id=pk)
    if form.is_valid():
        for attachment in form.save():
            mm = MediaManager(attachment)
            mm.process()
        return redirect('/{}/{}/'.format(model, pk))
    return render(request, 'resources/upload.html', locals())


@login_required
def download(request, pk):
    resource = get_object_or_404(Resource, id=pk)
    attachments = resource.get_attachments()
    return render(request, 'resources/download.html', locals())


@login_required
def download_attachment(request, pk, attachment_id):
    resource = get_object_or_404(Resource, id=pk)
    attachment = get_object_or_404(Attachment, id=attachment_id)

    if not resource.is_bought_by(request.user):
        return HttpResponseNotFound()

    with open(attachment.file.path, 'rb') as f:
        response = HttpResponse(content=f.read())
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment; filename={}'.format(
            f.name.split('/')[-1])
        return response

