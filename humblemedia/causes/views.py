from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.views.generic import ListView, FormView, DetailView, CreateView, UpdateView
from .models import Cause
from .forms import CauseForm

class OwnedViewMixin():
    pass


class AuthViewMixin:

    @classmethod
    def as_view(cls, *args, **kwargs):
        res = super().as_view(*args, **kwargs)
        return login_required(res)

class CauseList(ListView):

    model = Cause

    def get_queryset(self):
        return self.model.filter(is_published=True, is_verified=True)

class CauseDetails(DetailView):

    model = Cause

class CauseEdit(UpdateView):

    model = Cause



class CauseCreate(AuthViewMixin, CreateView):
    model = Cause
    form_class = CauseForm

    def get_success_url(self):
        return self.object.get_absolute_url()

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.creator = self.request.user
        obj.save()
        return super().form_valid(form)



