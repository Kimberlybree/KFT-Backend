from rest_framework import serializers
from .models import KeepFit

class KeepFitSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeepFit
        fields = ('id', 'title', 'goal_description', 'goal_completed')

                                      