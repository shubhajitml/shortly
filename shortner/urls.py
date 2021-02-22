from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(route="create", view=views.shortenUrl, name="create"),
    path(route="<str:hash_value>", view=views.redirectUrl, name="redirect"),
]
