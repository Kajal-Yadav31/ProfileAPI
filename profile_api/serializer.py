from rest_framework import serializers
from profile_api import models

class HelloSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=15)

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password' :{
                'write_only' : True,
                'style' : {'input_type': 'password'}
            }
        }

    def create(self, validated_date):
        user = models.UserProfile.objects.create_user(
            email = validated_date['email'],
            name = validated_date['name'],
            password = validated_date['password']
        )

        return user
    

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile' : {'read_only': True}}