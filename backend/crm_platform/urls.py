from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from crm_core import api
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register("companies", api.CompanyViewSet, basename="company")
router.register("contacts", api.ContactViewSet, basename="contact")
router.register("leads", api.LeadViewSet, basename="lead")
router.register("deals", api.DealViewSet, basename="deal")
router.register("activities", api.ActivityViewSet, basename="activity")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/ai/", include("crm_core.ai_urls")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

