from django.contrib import admin

from applications.doctor.models import Doctor, DoctorImage


class InLineDoctorImage(admin.TabularInline):
    model = DoctorImage
    extra = 1
    fields = ['image', ]


class DoctorAdminDisplay(admin.ModelAdmin):
    inlines = [InLineDoctorImage, ]


admin.site.register(Doctor, DoctorAdminDisplay)
