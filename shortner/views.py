from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
import validators
import uuid
from .models import Url
from django.http import HttpResponse
from django.contrib import messages


def index(request):
    return render(request, 'index.html')

def shortenUrl(request):
        if request.method == "POST":
            url = request.POST['link']
            if validators.url(url):
                if(Url.objects.filter(link=url).exists()):
                    uid = Url.objects.get(link=url).uuid
                else:
                    uid = str(uuid.uuid4())[:5]
                    new_url = Url(link=url, uuid=uid)
                    new_url.save()
                return HttpResponse(uid)
            else:
                messages.info(request, "Entered URL is not valid!")
                return HttpResponseRedirect('index.html')

def redirectUrl(request, hash_value):
    long_url_details = Url.objects.get(uuid=hash_value)
    return redirect(long_url_details.link)
