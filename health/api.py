from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from django.core import serializers
from datetime import datetime
from django.utils.dateformat import DateFormat

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

class DayStart(APIView):
    def get(self, request):
        queryset = Routine.objects.filter(routine_user=request.user, done=True)
        queryset.update(done=False)
        return Response(status=status.HTTP_200_OK)


class AllRoutineList(APIView):
    def get(self, request):
        model = Routine.objects.filter(routine_user=request.user, completed=False)
        serialized = RoutineSerializer(model, many=True)
        return Response(serialized.data)

    def post(self, request):
        serialized = RoutineSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors ,status=status.HTTP_400_BAD_REQUEST)

class DailyRoutineList(APIView):
    def get(self, request, day):
        today = DateFormat(datetime.now()).format('Y-m-d')
        model = Routine.objects.filter(routine_user=request.user, weekday__contains=day, done=False, completed=False, start_date__lte=today, end_date__gte=today)
        serialized = RoutineSerializer(model, many=True)
        return Response(serialized.data)

class RoutineDetail(APIView):
    def get(self, request, routine_id):
        model = Routine.objects.get(id=routine_id, routine_user=request.user)
        serialized = RoutineSerializer(model)
        return Response(serialized.data)

    def put(self, request, routine_id):
        model = Routine.objects.get(id=routine_id, routine_user=request.user)
        serialized = RoutineSerializer(model, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, routine_id):
        model = Routine.objects.get(id=routine_id, routine_user=request.user)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class WorkoutList(APIView):
    def get(self, request, routine_id):
        routine = Routine.objects.get(id=routine_id, routine_user=request.user)
        workout = routine.workout
        serialized = WorkoutSerializer(workout, many=True)
        return Response(serialized.data)

    def post(self, request, routine_id):
        routine = Routine.objects.get(id=routine_id, routine_user=request.user)
        workout = Workout.objects.create(routine_id=routine)
        serialized = WorkoutSerializer(workout, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors ,status=status.HTTP_400_BAD_REQUEST)

class WorkoutDetail(APIView):
    def get(self, request, routine_id, workout_id):

        model = Workout.objects.get(id=workout_id)
        serialized = WorkoutSerializer(model)
        return Response(serialized.data)
        
    def put(self, request, routine_id, workout_id):

        model = Workout.objects.get(id=workout_id)
        serialized = WorkoutSerializer(model, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, routine_id, workout_id):
        model = Workout.objects.get(id=workout_id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CompletedRoutine(APIView):
    def get(self, request):
        model = Routine.objects.filter(completed=True, routine_user=request.user)
        serialized = RoutineSerializer(model, many=True)
        return Response(serialized.data)

class SignUp(APIView):
    def post(self, request):
        user = User.objects.create_user(username=request.data['id'], password=request.data['password'])
        profile = Profile(user=user, nickname=request.data['nickname'])

        user.save()
        profile.save()
        token = Token.objects.create(user=user)
        return Response({"Token" : token.key})

class Login(APIView):
    def post(self, request):
        user = authenticate(username=request.data['id'], password=request.data['password'])
        if user is not None:
            token = Token.objects.get(user=user)
            return Response({"Token" : token.key})
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

class SignOut(APIView):#토큰전달필요
    def get(self, request):
        user = User.objects.get(username=request.user)
        token = Token.objects.get(user=user)
        token.delete()
        user.delete()
        print("deleted")
        return Response(status=status.HTTP_200_OK)