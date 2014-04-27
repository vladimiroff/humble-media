from django.shortcuts import render

from resources.models import Resource


def home(request):
    audios = Resource.audios.all()[:5]
    documents = Resource.documents.all()[:5]
    images = Resource.images.all()[:5]
    videos = Resource.videos.all()[:5]
    others = Resource.others.all()[:5]
    return render(request, "home.html", locals())
