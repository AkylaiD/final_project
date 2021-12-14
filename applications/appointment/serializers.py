from rest_framework import serializers


# from applications.appointment.models import TakeAppointment, Appointment
#
#
# class TakeAppointmentSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = TakeAppointment
#         fields = ('appointment', 'message', 'date_time')
#
#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         representation['doctor'] = f'{instance.doctor}'
#         return representation
from applications.appointment.models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    # items = TakeAppointmentSerializer(many=True, write_only=True, required=True)
    # total_cost = serializers.DecimalField(max_digits=100, decimal_places=2, default=0)
    full_name = serializers.CharField(max_length=100, required=True)
    phone_number = serializers.CharField(max_length=100, required=True)

    class Meta:
        model = Appointment
        # fields = ('full_name', 'contact_number', 'total_cost', 'items')
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        # items = validated_data.pop('items')
        # total_cost = 0
        if request.user.is_authenticated:
            validated_data['user_id'] = request.user.id
        appointment = Appointment.objects.create(**validated_data)
        # for item in items:
        #     doctor = item['doctor']
        #     take_appointment = TakeAppointment.objects.create(appointment=appointment, doctor=doctor)
        #     total_cost += take_appointment.total_cost
        # appointment.total_cost = total_cost
        appointment.save()
        return appointment

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['doctors'] = AppointmentSerializer(Appointment.objects.filter(appointment=instance.id), many=True).data
    #     return representation

