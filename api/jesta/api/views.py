from rest_framework import viewsets

from .serializers import ElderSerializer, ProSerializer, SonSerializer, ProfessionSerializer
from .models import Elder, Son, Profession, Pro


class ElderViewSet(viewsets.ModelViewSet):
    queryset = Elder.objects.all().order_by('second_name')
    serializer_class = ElderSerializer

class SonViewSet(viewsets.ModelViewSet):
    queryset = Son.objects.all().order_by('second_name')
    serializer_class = SonSerializer

class ProfessionViewSet(viewsets.ModelViewSet):
    queryset = Profession.objects.all().order_by('title')
    serializer_class = ProfessionSerializer

class ProViewSet(viewsets.ModelViewSet):
    queryset = Pro.objects.all().order_by('second_name')
    serializer_class = ProSerializer