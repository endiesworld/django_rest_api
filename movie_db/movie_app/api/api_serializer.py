from rest_framework import serializers
from movie_app.models import WatchList, StreamPlatform


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     decription = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.decription = validated_data.get(
#             'decription', instance.decription)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

#     def validate_name(slef, value):
#         if len(value) < 3:
#             raise serializers.ValidationError('Movie name too short')
#         else:
#             return value

#     def validate(self, data):
#         """
#         Check that start is before finish.
#         """
#         if data['name'] == data['decription']:
#             raise serializers.ValidationError(
#                 "Movie name and description cannot be the same")
#         return data

class WatchListSerializer(serializers.ModelSerializer):

    # len_name = serializers.SerializerMethodField()

    class Meta:
        model = WatchList
        fields = "__all__"
        # fields = ['id', 'name', 'decription']
        # exclude = ['active']

    # def get_len_name(self, object):
    #     return len(object.name)

    # def validate_name(slef, value):
    #     if len(value) < 3:
    #         raise serializers.ValidationError('Movie name too short')
    #     else:
    #         return value

    # def validate(self, data):
    #     """
    #     Check that start is before finish.
    #     """
    #     if data['name'] == data['decription']:
    #         raise serializers.ValidationError(
    #             "Movie name and description cannot be the same")
    #     return data


# ====================== SERIALIZER CLASS FOR StreamPlatform ======================


class StreamPlatformSerializer(serializers.ModelSerializer):

    # len_name = serializers.SerializerMethodField()

    class Meta:
        model = StreamPlatform
        fields = "__all__"
