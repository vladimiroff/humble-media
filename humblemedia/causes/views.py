from django.views.generic import ListView
from humblemedia.causes.models import Cause


class CauseList(ListView):

    model = Cause

    def get_queryset(self):
        return self.model.filter(is_published=True, is_verified=True)
