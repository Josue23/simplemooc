from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

	# caminho do arquivo simplemooc/core/urls.py
    url(r'^', include('simplemooc.core.urls', namespace='core')),

    url(r'^admin/', include(admin.site.urls)),
)



'''
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'simplemooc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
'''