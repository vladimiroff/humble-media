from django.contrib.auth.models import User
from django.db.models import Count
from django.views.generic import TemplateView
from causes.models import Cause
from resources.models import Resource


class Home(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        cont = {}
        cont['audios'] = Resource.audios.all()[:5]
        cont['documents'] = Resource.documents.all()[:5]
        cont['images'] = Resource.images.all()[:5]
        cont['videos'] = Resource.videos.all()[:5]
        cont['others'] = Resource.others.all()[:5]
        cont['top_contributors'] = User.objects.annotate(resource_count=Count("resources")).order_by("-resource_count")[:10]
        cont['top_donators'] = User.objects.annotate(resource_count=Count("resources")).order_by("resource_count")[:10]
        cont['number_causes'] = Cause.objects.all().count()
        cont['donations_received'] = None
        return cont

