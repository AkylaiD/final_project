from django.urls import path

from applications.doctor.views import DoctorListView, DoctorDetailView

urlpatterns = [
    path('doctors-list/', DoctorListView.as_view()),
    path('doctors-list/<int:pk>/', DoctorDetailView.as_view()),

]