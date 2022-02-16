from rest_framework import serializers

from .models import Elder, Pro, Son, Profession


class ElderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Elder
        fields = ('first_name', 'second_name', 'city', 'phone_number', 'id')

class SonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Son
        fields = ('first_name', 'second_name', 'city', 'phone_number', 'age', 'id', 'elder')

class ProfessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profession
        fields = ('title',)

class ProSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pro
        fields = ('first_name', 'second_name', 'city', 'phone_number', 'id', 'profession')