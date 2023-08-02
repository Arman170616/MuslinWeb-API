from rest_framework import serializers

from .models import AboutUs


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'

        def update(self, instance, validated_data):
            instance.description = validated_data.get('description', instance.description)
            instance.save()
            return instance