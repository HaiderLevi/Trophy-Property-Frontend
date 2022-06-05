from rest_framework import serializers
from society.models import Plot, Video

# class CitySerializer(serializers.ModelSerializer):

#     class Meta:
#         model = City
#         fields = ['id', 'name']

# class SocietySerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Society
#         fields = ['id', 'name', 'city']

class PlotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plot
        fields = '__all__'

# class SocietyDetailSerializer(serializers.ModelSerializer):

#     city = CitySerializer(read_only=True)

#     class Meta:
#         model = Society
#         fields = ['id', 'name', 'city']

class PlotDetailSerializer(serializers.ModelSerializer):

    # society = SocietySerializer(read_only=True)

    class Meta:
        model = Plot
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = '__all__'


class VideoDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = '__all__'
