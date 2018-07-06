from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    path('<platform>/<btag>', hello.views.index, name='index'),
    path('*', hello.views.notFound, name='notFound'),
    url(r'^$', hello.views.notFound, name='notFound'),
    url(r'^*$', hello.views.notFound, name='notFound'),
    url(r'^/*$', hello.views.notFound, name='notFound'),
    url(r'*', hello.views.notFound, name='notFound'),
]
