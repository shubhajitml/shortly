from django.shortcuts import render, redirect
import uuid
from .models import Url
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')


def shortenUrl(request):
    if request.method == "POST":
        url = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link=url, uuid=uid)
        new_url.save()
        return HttpResponse(uid)


def redirectUrl(request, hash_value):
    long_url_details = Url.objects.get(uuid=hash_value)
    return redirect(long_url_details.link)
