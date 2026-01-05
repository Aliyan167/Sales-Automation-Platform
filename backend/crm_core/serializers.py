from rest_framework import serializers
from .models import Company, Contact, Lead, Deal, Activity

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["id", "name", "website", "created_at"]

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ["id", "company", "name", "email", "title"]

class LeadSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    company_id = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all(), source="company", write_only=True)

    class Meta:
        model = Lead
        fields = ["id", "company", "company_id", "contact", "title", "value", "probability", "status", "created_at", "owner"]
        read_only_fields = ["created_at"]

class DealSerializer(serializers.ModelSerializer):
    lead = LeadSerializer(read_only=True)
    lead_id = serializers.PrimaryKeyRelatedField(queryset=Lead.objects.all(), source="lead", write_only=True)

    class Meta:
        model = Deal
        fields = ["id", "lead", "lead_id", "name", "value", "stage", "probability", "created_at"]
        read_only_fields = ["created_at"]

class ActivitySerializer(serializers.ModelSerializer):
    lead = LeadSerializer(read_only=True)
    lead_id = serializers.PrimaryKeyRelatedField(queryset=Lead.objects.all(), source="lead", write_only=True)

    class Meta:
        model = Activity
        fields = ["id", "lead", "lead_id", "actor", "activity_type", "notes", "occurred_at", "created_at"]
        read_only_fields = ["created_at"]

