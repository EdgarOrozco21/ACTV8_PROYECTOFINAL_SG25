from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('materiales/', views.ver_materiales, name='ver_materiales'),
    path('materiales/agregar/', views.agregar_material, name='agregar_material'),
    path('materiales/editar/<int:material_id>/', views.editar_material, name='editar_material'),
    path('materiales/borrar/<int:material_id>/', views.borrar_material, name='borrar_material'),

    path('centros/', views.ver_centros, name='ver_centros'),
    path('centros/agregar/', views.agregar_centro, name='agregar_centro'),
    path('centros/editar/<int:centro_id>/', views.editar_centro, name='editar_centro'),
    path('centros/borrar/<int:centro_id>/', views.borrar_centro, name='borrar_centro'),

    path('donantes/', views.ver_donantes, name='ver_donantes'),
    path('donantes/agregar/', views.agregar_donante, name='agregar_donante'),
    path('donantes/editar/<int:donante_id>/', views.editar_donante, name='editar_donante'),
    path('donantes/borrar/<int:donante_id>/', views.borrar_donante, name='borrar_donante'),

    path('empleados/', views.ver_empleados, name='ver_empleados'),
    path('empleados/agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('empleados/editar/<int:empleado_id>/', views.editar_empleado, name='editar_empleado'),
    path('empleados/borrar/<int:empleado_id>/', views.borrar_empleado, name='borrar_empleado'),

    path('recepciones/', views.ver_recepciones, name='ver_recepciones'),
    path('recepciones/agregar/', views.agregar_recepcion, name='agregar_recepcion'),
    path('recepciones/editar/<int:recepcion_id>/', views.editar_recepcion, name='editar_recepcion'),
    path('recepciones/borrar/<int:recepcion_id>/', views.borrar_recepcion, name='borrar_recepcion'),
]
