from rest_framework import serializers

from app.models import Mitbrand


class MitbrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mitbrand
        fields = '__all__'
