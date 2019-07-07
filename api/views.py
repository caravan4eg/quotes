# api/views.py
from rest_framework import generics
from django_app.models import Quote
from .serializers import QuoteSerializer


class QuoteAPIView(generics.ListAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
