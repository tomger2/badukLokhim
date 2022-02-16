from rest_framework import viewsets

from .serializers import ElderSerializer, ProSerializer, SonSerializer, ProfessionSerializer, CallSerializer
from .models import Elder, Son, Profession, Pro, Call


class ElderViewSet(viewsets.ModelViewSet):
    queryset = Elder.objects.all().order_by('name')
    serializer_class = ElderSerializer

class SonViewSet(viewsets.ModelViewSet):
    queryset = Son.objects.all().order_by('name')
    serializer_class = SonSerializer

class ProfessionViewSet(viewsets.ModelViewSet):
    queryset = Profession.objects.all().order_by('title')
    serializer_class = ProfessionSerializer

class ProViewSet(viewsets.ModelViewSet):
    queryset = Pro.objects.all().order_by('name')
    serializer_class = ProSerializer

class CallViewSet(viewsets.ModelViewSet):
    queryset = Call.objects.all().order_by('start_date')
    serializer_class = CallSerializer