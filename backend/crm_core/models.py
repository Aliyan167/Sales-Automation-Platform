from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Company(models.Model):
    name = models.CharField(max_length=255)
    website = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Contact(models.Model):
    company = models.ForeignKey(Company, related_name="contacts", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    title = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.name} ({self.company.name})"

class Lead(models.Model):
    STATUS_NEW = "new"
    STATUS_CONTACTED = "contacted"
    STATUS_QUALIFIED = "qualified"
    STATUS_WON = "won"
    STATUS_LOST = "lost"
    STATUS_CHOICES = [
        (STATUS_NEW, "New"),
        (STATUS_CONTACTED, "Contacted"),
        (STATUS_QUALIFIED, "Qualified"),
        (STATUS_WON, "Won"),
        (STATUS_LOST, "Lost"),
    ]

    company = models.ForeignKey(Company, related_name="leads", on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, related_name="leads", on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=255, blank=True)
    value = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    probability = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default=STATUS_NEW)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, related_name="leads", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Lead {self.title} ({self.company.name})"

class Deal(models.Model):
    lead = models.ForeignKey(Lead, related_name="deals", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=12, decimal_places=2)
    stage = models.CharField(max_length=255, default="Proposal")
    probability = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Deal {self.name} - {self.lead.company.name}"

class Activity(models.Model):
    TYPE_CALL = "call"
    TYPE_MEETING = "meeting"
    TYPE_EMAIL = "email"
    TYPE_CHOICES = [
        (TYPE_CALL, "Call"),
        (TYPE_MEETING, "Meeting"),
        (TYPE_EMAIL, "Email"),
    ]

    lead = models.ForeignKey(Lead, related_name="activities", on_delete=models.CASCADE)
    actor = models.ForeignKey(User, related_name="activities", on_delete=models.SET_NULL, null=True, blank=True)
    activity_type = models.CharField(max_length=32, choices=TYPE_CHOICES)
    notes = models.TextField(blank=True)
    occurred_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Activity {self.activity_type} for {self.lead}"

