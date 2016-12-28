from django.conf.urls import url

from . import views

import crud1

app_name = 'crud1'

urlpatterns = [
	#ruta para eliminar
    	url(r'^hackenings/(?P<hackeningid>\d+)/delete/', crud1.views.delete_hackening, name='delete_hackening'),
	#listado
	url(r'^$', crud1.views.hackenings, name='list_hackenings'),
	#listado
	url(r'^hackenings/list', crud1.views.hackenings, name='list_hackenings'),
	#formulario para añadir
	url(r'^hackenings/add/', crud1.views.add_hackening, name='add_hackening'),
	#formulario para editar
	url(r'^hackenings/(?P<hackeningid>\d+)/', crud1.views.update_hackening, name='update_hackening')
]
	
