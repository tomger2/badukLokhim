from rest_framework import serializers

from .models import Call, Elder, Pro, Son, Profession


class ElderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Elder
        fields = ('name', 'age', 'city', 'address', 'private_home', 'apartment_num', 'floor', 'phone')

class SonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Son
        fields = ('name', 'phone', 'id', 'elder')

class ProfessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profession
        fields = ('title',)

class ProSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pro
        fields = ('name', 'active_cities', 'phone', 'id', 'profession', 'rank', 'num_of_calls')

class CallSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Call
        fields = ('elder', 'grandson', 'is_open', 'is_occupied', 'description', 'handy_man_pool', 'handy_man', 'cost', 'start_date', 'closed_date', 'destination', 'profession', 'id')