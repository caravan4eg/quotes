# api/serializers.py
from rest_framework import serializers
from django_app.models import Quote


class QuoteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Quote
        fields = '__all__'