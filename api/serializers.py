from api.models import Prognose, Trend, Info
from rest_framework import serializers


#         Scenario 1
# ---------------------------

class PrognoseSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Prognose
        fields = ('sector','branche','head','body')

class TrendSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Trend
        fields = ('sector','branche','head','body')

class InfoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Info
        fields = ('sector','branche','body')

