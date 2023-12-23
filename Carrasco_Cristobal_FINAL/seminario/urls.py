from django.urls import path
from .views import InscritoList, Form_Inscrito, institucion_list, Institucion_Form
from .views import MisDatos


urlpatterns = [
    path('inscritos/', InscritoList.as_view(), name='inscrito-list'),
    path('inscritos/form/', Form_Inscrito.as_view(), name='inscrito-form'),
    path('instituciones/', institucion_list, name='institucion-list'),
    path('instituciones/form/', Institucion_Form.as_view(), name='institucion-form'),
    path('autor/', MisDatos.as_view(), name='mis-datos'),


]
