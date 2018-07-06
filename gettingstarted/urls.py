from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

import hello.views

urlpatterns = [
    path('<platform>/<btag>', hello.views.index, name='index'),
    # url(r'^.*$', hello.views.notFound, name='notFound'),
]

urlpatterns += staticfiles_urlpatterns()
