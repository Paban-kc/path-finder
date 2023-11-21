from rest_framework import serializers

from ...model import Vacancy

class VacancyUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        exclude = ('organization',)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
