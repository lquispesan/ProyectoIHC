from django.urls import path
from alumnos.views.alumnos.views import *

app_name="alumnos"

urlpatterns =[ 
	path('list/', AlumnoListView.as_view(), name="lista"),
	path('add/' ,AlumnoCreateView.as_view(), name="crear"),
	path('edit/<int:pk>/', AlumnoUpdateView.as_view() , name="editar"),
	path('delete/<int:pk>/', AlumnoDeleteView.as_view() , name="eliminar"),
	path('graphics/', graphics, name='graphics'),
	path('graphics/g1', graphics_g1, name="graphic1"),
	path('graphics/g2', graphics_g2, name="graphic2"),
	path('graphics/g3', graphics_g3, name="graphic3"),
	path('graphics/g4', graphics_g4, name="graphic4"),
	path('graphics/g5', graphics_g5, name="graphic5"),


]