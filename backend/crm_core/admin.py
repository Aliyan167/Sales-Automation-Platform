from django.contrib import admin
from .models import Company, Contact, Lead, Deal, Activity, Membership, Subscription

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "website", "created_at")

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "company")

@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ("user", "company", "role", "is_active", "created_at")
    list_filter = ("role", "is_active")

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("company", "plan", "status", "start_date", "end_date")
    list_filter = ("plan", "status")

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("title", "company", "status", "value", "probability", "owner", "created_at")
    list_filter = ("status",)

@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = ("name", "lead", "value", "stage", "probability", "created_at")

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ("activity_type", "lead", "actor", "occurred_at", "created_at")

