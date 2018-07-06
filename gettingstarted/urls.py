from django.urls import path

from django.contrib import admin
admin.autodiscover()

import hello.views

urlpatterns = [
    path('<platform>/<btag>', hello.views.index, name='index'),
    path('*', hello.views.notFound, name='notFound')
]
