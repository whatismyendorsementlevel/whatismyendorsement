from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import hello.views

urlpatterns = [
    path('<platform>/<btag>', hello.views.index, name='index'),
    # url(r'^.*$', hello.views.notFound, name='notFound'),
]
