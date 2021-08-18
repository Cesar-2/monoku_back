from rest_framework import serializers
from ..models import BandasSimilares


class BandasSimilaresSerializer(serializers.ModelSerializer):
    class Meta:
        model = BandasSimilares
        fields = '__all__'
