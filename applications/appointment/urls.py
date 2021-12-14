from django.urls import path
from rest_framework.routers import DefaultRouter

from applications.appointment.views import AppointmentViewSet

router = DefaultRouter()
router.register('appointment', AppointmentViewSet)
urlpatterns = [
    # path('appointments-list/', AppointmentViewSet),
    # path('appointments-list/<int:pk>/', AppointmentViewSet)
]
urlpatterns.extend(router.urls)