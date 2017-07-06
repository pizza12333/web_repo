from rest_framework import serializers
from rest_api.models import ChickenData

class ChickenSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChickenData
        fields = ('id','date', 'year', 'month', 'day', 'day_of_weeks', 'gender', 'age', 'loc_mid', 'call')
