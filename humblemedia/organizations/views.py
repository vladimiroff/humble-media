from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Organization
from .forms import OrganizationForm

@login_required
def add_organization(request):
    data = request.POST if request.POST else None
    form = OrganizationForm(data, user=data['admins'][0])
    if form.is_valid():
        form.save()
        return redirect('organizations/{}'.format(form.instance.pk))
    return render(request, 'organization/add.html', locals())
