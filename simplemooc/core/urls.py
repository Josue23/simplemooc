from django.conf.urls import patterns, include, url

# patterns('simplemooc.core.views' - o Django usa como um prefixo em todas as urls
	# simplemooc é o projeto
	# core é a app
	# views é o arquivo views.py
	# home é o nome da funçao no arquivo views.py
	# contact é o nome da funçao no arquivo views.py
urlpatterns = patterns('simplemooc.core.views',
    url(r'^$', 'home', name='home'),
    url(r'^contato/$', 'contact', name='contact'),
)