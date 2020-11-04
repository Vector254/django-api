from rest_framework import serializers
from .models import Profile, Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id','title','link', 'description', 'date_posted')

