from rest_framework import serializers
from movie_app.models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    decription = serializers.CharField()
    active = serializers.BooleanField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.decription = validated_data.get(
            'decription', instance.decription)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance
