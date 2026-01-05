from rest_framework import viewsets, permissions
from .models import Company, Contact, Lead, Deal, Activity
from .serializers import CompanySerializer, ContactSerializer, LeadSerializer, DealSerializer, ActivitySerializer

class IsAuthenticatedOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    pass

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all().select_related('company', 'contact', 'owner')
    serializer_class = LeadSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class DealViewSet(viewsets.ModelViewSet):
    queryset = Deal.objects.all().select_related('lead')
    serializer_class = DealSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all().select_related('lead', 'actor')
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

