from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import JsonResponse

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import Inscrito, Institucion
from .serializers import InscritoSerializer, InstitucionSerializer
from .forms import InscritoForm, InstitucionForm


def index(request):
    return render(request, 'seminario/index.html')

class MisDatos(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        autor_data = {
            'nombres': 'Cristóbal Sebastian',
            'apellidos': 'Carrasco Inzunza',
            'correo': 'cristobal.carrasco15@inacapmail.cl',
            'edad': '22',
        }
        return Response(autor_data)
    
#-------------Inscrito-------------#

class InscritoList(generics.ListCreateAPIView):
    queryset = Inscrito.objects.all()
    serializer_class = InscritoSerializer

class Form_Inscrito(View):
    def get(self, request):
        form = InscritoForm()
        return render(request, 'seminario/inscrito_form.html', {'form': form})

    def post(self, request):
        form = InscritoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inscrito-list')
        return render(request, 'seminario/inscrito_form.html', {'form': form})
    

#-------------Institucon-------------#

    
class Institucion_Form(View):
    def get(self, request):
        form = InstitucionForm()
        return render(request, 'seminario/institucion_form.html', {'form': form})

    def post(self, request):
        form = InstitucionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('institucion-list') 
        return render(request, 'seminario/institucion_form.html', {'form': form})
    
def institucion_list(request):
    instituciones = Institucion.objects.all()
    serializer = InstitucionSerializer(instituciones, many=True)
    return JsonResponse(serializer.data, safe=False)  