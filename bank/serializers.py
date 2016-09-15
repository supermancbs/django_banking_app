from django.contrib.auth.models import User, Withdrawl
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    tracks = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ('name', 'amount', 'withdrawls')
