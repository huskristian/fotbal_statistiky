from rest_framework import viewsets
from .models import Tym, Hrac, Zapas, StatistikyZapasu
from .serializers import TymSerializer, HracSerializer, ZapasSerializer, StatistikyZapasuSerializer

class TymViewSet(viewsets.ModelViewSet):
    queryset = Tym.objects.all()
    serializer_class = TymSerializer

class HracViewSet(viewsets.ModelViewSet):
    queryset = Hrac.objects.all()
    serializer_class = HracSerializer

class ZapasViewSet(viewsets.ModelViewSet):
    queryset = Zapas.objects.all()
    serializer_class = ZapasSerializer

class StatistikyZapasuViewSet(viewsets.ModelViewSet):
    queryset = StatistikyZapasu.objects.all()
    serializer_class = StatistikyZapasuSerializer
