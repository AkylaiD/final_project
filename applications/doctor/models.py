from django.db import models

from applications.department.models import Department


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='doctor')
    experience_description = models.TextField()
    work_experience = models.PositiveSmallIntegerField()
    price_per_visit = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class DoctorImage(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.doctor.name



