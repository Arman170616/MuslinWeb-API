from rest_framework import serializers

from .models import AboutUs, ContactInformation, Product


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'

        def update(self, instance, validated_data):
            instance.description = validated_data.get('description', instance.description)
            instance.save()
            return instance
        


class ContactInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInformation
        fields = '__all__'

        def create(self, validated_data):
            return ContactInformation.objects.create(**validated_data)
        


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','name', 'description', 'price', 'image')