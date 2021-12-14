from rest_framework import serializers

from applications.doctor.models import Doctor, DoctorImage
from applications.review.serializers import ReviewSerializer


class DoctorImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = DoctorImage
        fields = ('image', )

    def _get_image_url(self, obj):
        if obj.image:
            url = obj.image.url
            # print(url)
            request = self.context.get('request')
            if request is not None:
                url = request.build_absolute_uri(url)
                # print(url)
        else:
            url = ''
        return url

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = self._get_image_url(instance)
        return representation


class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # print(instance.review.all())
        total_rating = [i.rating for i in instance.review.all()]
        if len(total_rating) > 0:
            representation['total_rating'] = sum(total_rating) / len(total_rating)
        representation['images'] = DoctorImageSerializer(DoctorImage.objects.filter(doctor=instance.id), many=True, context=self.context).data
        return representation


class DoctorDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        total_rating = [i.rating for i in instance.review.all()]
        if len(total_rating) > 0:
            representation['total_rating'] = sum(total_rating) / len(total_rating)
        representation['images'] = DoctorImageSerializer(DoctorImage.objects.filter(doctor=instance.id), many=True,
                                                          context=self.context).data
        representation['reviews'] = ReviewSerializer(instance.review.filter(doctor=instance.id), many=True).data
        return representation
