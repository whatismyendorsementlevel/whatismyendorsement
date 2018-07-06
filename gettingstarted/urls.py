from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    path('/<string:platform>/<string:btag>, hello.views.index')
    # url(r'^$', hello.views.index, name='index'),
    # url(r'(?P<platform>\w+)(?P<btag>\w+)/$', hello.views.index, name='index')
]
