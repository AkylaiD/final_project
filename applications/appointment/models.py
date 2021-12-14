from django.db import models
from django.utils import timezone

from applications.account.models import User
from applications.department.models import Department
from applications.doctor.models import Doctor


class Appointment(models.Model):

    TIMESLOT_LIST = (
        (0, '09:00 – 09:30'),
        (1, '10:00 – 10:30'),
        (2, '11:00 – 11:30'),
        (3, '12:00 – 12:30'),
        (4, '13:00 – 13:30'),
        (5, '14:00 – 14:30'),
        (6, '15:00 – 15:30'),
        (7, '16:00 – 16:30'),
        (8, '17:00 – 17:30'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointment')
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    date = models.DateField(default=timezone.now, help_text="DD.MM.YYYY")
    timeslot = models.IntegerField(choices=TIMESLOT_LIST, default=0)
    # department = models.ForeignKey(Department, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctor')
    message = models.TextField(default="")
    # created_at = models.DateTimeField(default=timezone.now)


    # class Meta:
    #     unique_together = ('doctor', 'date', 'timeslot')

    def __str__(self):
        # return self.full_name
        return '{} {} {}. User: {}'.format(self.date, self.time, self.doctor, self.full_name)

    @property
    def time(self):
        return self.TIMESLOT_LIST[self.timeslot][1]

#     def save(self, *args, **kwargs):
#         self.total_cost = self.doctor.price_per_visit
#         super(Appointment, self).save(*args, **kwargs)
# #
# class TakeAppointment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
#     full_name = models.CharField(max_length=100)
#     message = models.TextField(default="", blank=True)
#     phone_number = models.CharField(max_length=120)
#     date_time = models.DateTimeField(default=timezone.now)
#
#     def __str__(self):
#         return self.full_name
#
#     def save(self, *args, **kwargs):
#         self.total_cost = self.doctor.price_per_visit
#         super(TakeAppointment, self).save(*args, **kwargs)
