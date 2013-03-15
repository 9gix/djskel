from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

class HomeView(TemplateView):
    template_name = 'index.html'

home = HomeView.as_view()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home, name='home'),
)
