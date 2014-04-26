from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Organization
from .forms import OrganizationForm


@login_required
def add(request):
    data = request.POST if request.POST else None
    form = OrganizationForm(data, user=request.user)
    if form.is_valid():
        form.save()
        return redirect('organizations/{}'.format(form.instance.pk))
    return render(request, 'organizations/add.html', locals())


@login_required
def edit(request, pk=None):
    organization = get_object_or_404(Organization, id=pk)
    if request.user in organization.admins.all():
        data = request.POST if request.POST else None
        form = OrganizationForm(data, user=request.user, instance=organization)
        if form.is_valid():
            form.save()
            return redirect('organizations/{}'.format(form.instance.pk))
        return render(request, 'organizations/edit.html', locals())
    else:
        return redirect('organizations/list')


def view(request, pk=None):
    organization = get_object_or_404(Organization, id=pk)
    return render(request, 'organizations/view.html', locals())


@login_required
def delete(request, pk=None):
    organization = get_object_or_404(Organization, id=pk)
    if request.user in organization.admins.all():
        organization.delete()
    return redirect('organizations/list')


def list(request):
    organizations = Organization.objects.all()
    return render(request, 'organizations/list.html', locals())
