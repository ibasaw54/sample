from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class WorkoutSerializer(serializers.ModelSerializer) :
    workout_name = serializers.CharField(required=False)
    weight = serializers.IntegerField(required=False)
    repetition = serializers.IntegerField(required=False)
    sets = serializers.IntegerField(required=False)
    class Meta:
        model = Workout
        fields = ("id", "workout_name", "weight", "repetition", "sets")


class RoutineSerializer(serializers.ModelSerializer) :
    workout = WorkoutSerializer(many=True, read_only=True, required=False)  
    routine_user = serializers.CharField(required=False)
    routine_name = serializers.CharField(required=False)
    start_date = serializers.DateField(required=False)
    end_date = serializers.DateField(required=False)
    weekday = serializers.CharField(required=False)
    done = serializers.BooleanField(required=False)
    completed = serializers.BooleanField(required=False)
    class Meta:
        model = Routine
        fields = ("id", "routine_user", "routine_name", "start_date", "end_date", "workout", "weekday", "done", "completed")
