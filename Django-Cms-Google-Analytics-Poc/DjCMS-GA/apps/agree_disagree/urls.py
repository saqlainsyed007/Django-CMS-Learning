from django.conf.urls import url, patterns
from . import views


urlpatterns = patterns('',
    url(r'^updateSelection/(?P<pk>[0-9]+)/(?P<sel>[0-9]+)/$',
        views.update_selection),
)
