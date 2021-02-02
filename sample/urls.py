"""sample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from health.api import *


urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),

    path('signup/', SignUp.as_view(), name='sign-up'),
    path('login/', Login.as_view(), name='log-in'),
    path('signout/', SignOut.as_view(), name='sign-out'),

    path('admin/', admin.site.urls),
    path('completed-routines', CompletedRoutine.as_view(), name='completed-routines'),
    path('daily-routines/<str:day>', DailyRoutineList.as_view(), name='daily-routines'),

    path('routines/all', AllRoutineList.as_view(), name='all-routines'),
    path('routines/<int:routine_id>', RoutineDetail.as_view(), name='routine-detail'),
    path('routines/<int:routine_id>/workouts', WorkoutList.as_view(), name='workout-list'),
    path('routines/<int:routine_id>/workouts/<int:workout_id>', WorkoutDetail.as_view(), name='workout-detail'),

    path('newday', DayStart.as_view(), name='daystart'),    
]