from django.db import models
from datetime import datetime
from django.utils.dateformat import DateFormat
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=10)

class Routine(models.Model) :
    id = models.AutoField(primary_key=True)
    routine_user = models.CharField(max_length=30, default='no users')
    routine_name = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField()
    weekday = models.CharField(max_length=40, default="Mon", blank=True, null=False)
    done = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

class Workout(models.Model) :
    id = models.AutoField(primary_key=True)
    workout_name = models.CharField(max_length=30, null=True)
    weight = models.IntegerField(default=0)
    repetition = models.IntegerField(default=0)
    sets = models.IntegerField(default=0)
    routine_id = models.ForeignKey("Routine", related_name="workout", on_delete=models.CASCADE, db_column="routine_id")

"""
class CompletedRoutine(Routine) :
    feedback = models.CharField(max_length=100)

class DailyReport(models.Model) :
    day = models.DateField(default=DateFormat(datetime.now()).format('Ymd'))
    routines = models.TextField(max_length=100)
"""