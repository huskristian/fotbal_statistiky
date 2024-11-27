from rest_framework import serializers
from .models import Tym, Hrac, Zapas, StatistikyZapasu

class TymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tym
        fields = '__all__'

class HracSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hrac
        fields = '__all__'

class ZapasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zapas
        fields = '__all__'

class StatistikyZapasuSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatistikyZapasu
        fields = '__all__'
