# Create your views here.
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, ListView
from .forms import CustomUserCreationForm,   MyfitnessForm, MyfoodgroupsForm

from .forms import BeginpageForm, MyfoodsuggestionsForm
# from .forms import MyallergicfoodsForm

# from .forms import MyallergicfoodsverForm

from .forms import HealthsymForm
# from .forms import MytrigfoodsForm
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views import generic
from django.contrib.auth.decorators import login_required

# from .models import Goals_ver
# from .models import CustomRole
# from .models import StaffUser
from .forms import StudyForm
from .forms import MydailylogForm


from .models import Myhealthscreening
# from .models import Myhealthscreening_ver
from .models import Myfitness

from .models import Dietician_note

from .models import Healthsym

# from .models import Majorsym

from .models import Study
from .models import Myexpenses

from .models import Myhabits
from .models import CustomUser
from .models import Supplements

from .models import Healthsym


from .models import Myfoodgroups

# from .models import Myfastfoods


from .models import Myallergicfoods

# from .models import Mytrigfoods
from .models import Mytypmeals1
# from .models import Mytypmeals2
# from .models import Mytyplunch
# from .models import Mytypdinner
from .models import Beginpage
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render
from rest_framework import generics

# from .serializers import GoalsSerializer
from django.core import serializers
# from .serializers import ProfileSerializer
from django.http import JsonResponse,HttpResponse

# from .models import CustomerForm
from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import StaffRegistrationForm
from django.http import HttpResponseRedirect
# from .forms import UpdateUserAuthForm

from .forms import HealthsymForm
from .forms import MyexpensesForm
from .forms import MyhealthscreeningForm
# from .forms import MyhealthscreeningverForm
from .forms import MyhabitsForm
# from .forms import MytrigfoodsForm
from .forms import Mytypmeals1Form
from .forms import SupplementsForm
# from .forms import Mytypmeals2Form
# from .forms import MylunchForm
# from .forms import MydinnerForm
from .forms import  DieticiannoteForm
from django.db.models import Q

from django.contrib.auth.decorators import login_required
from django.utils import timezone
import os

import dash
from dash import dcc

import pandas as pd
import plotly.graph_objects as go

import pandas as pd
import tkinter

from pandas import Series, DataFrame
import csv
import plotly.express as px
import seaborn as sns

from io import BytesIO
import base64

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

from django.contrib.auth import login, authenticate

from django.contrib.auth.models import Group, Permission


# from django.contrib.auth.views import login

import datetime

# class LoginView(TemplateView):
#   success_url = reverse_lazy('landing')
#   template_name = 'login.html'

# class SignUpView(generic.CreateView):
#   form_class = CustomUserCreationForm
#   success_url = reverse_lazy('login')
#   return redirect('/login') 
#   template_name = 'signup.html'

# def UpdateUserAuthView(request):
#   form=UpdateUserAuthForm(request.POST or None)
#   userData=CustomUser.objects.get(pk=request.user.id)
#   context={
#     'form':form,
#     'userData':userData
#   }
  
#   if form.is_valid():
#     print('form valid')
#     obj=form.cleaned_data
#     #remove form.is_valid and just check if exists 
#   if obj['username']:
#     userData.username=obj['username']
#     userData.address_1=obj['address_1']
#     userData.address_2=obj['address_2']
#     userData.city=obj['city']
#     userData.state=obj['state']
#     userData.zipcode=obj['zipcode']
#     # userData.phone_number=obj['phone_number']
#     userData.email=obj['email']
#     userData.save()
#     context={'form':form}
#     login(request,request.user)
#     return redirect('Goals')
#   print(form.errors)   
#   return render(request,'customUserUpdateView.html',context=context)

#   return render(request,"login.html",context,status)

# class MyLoginView(LoginView):
#     template_name = 'login.html'

class MyLoginView(LoginView):
    def form_valid(self, form):
        user = form.get_user()
        print("inside myloginview")
        print(user.last_login)
        print(user.role)
        user = CustomUser.objects.get(pk=user.id)
        print(user)
        context={'form':form}
        if (not user.last_login) and (user.role !='dietician'):
            print("First login!")
            template_name = 'myfoodgroups.html'
            return render(self.request,'myfoodgroups.html', context=context)
            
        else:
            return super().form_valid(form)

def testauthview(request):
    if request.user.is_authenticated:
        print(request.user)
        print(request.user.username)
        return HttpResponse("User is authenticated")
    else:
        return HttpResponse("User is not authenticated")            
 
# def flashpageView(request):
#   if request.user.is_authenticated:
#     print(request.user)
#     # Your logic for the flash page
#     return render(request, 'flashpage.html')   

# def flashpageView(request):
#   # if request.user.is_authenticated:
#   #   print(request.user)
#   #   print(request.user.is_active)
#   #   print(request.user.is_staff)
#     # Your logic for the flash page
#     return render(request, 'flashpage.html')
  # else:
  #   return redirect('login')  # 

# def MyfoodgroupsView(request):
  
#   if request.user.is_authenticated:
#         print(request.user)
#   if request.method == 'GET':
#     print("get")
    
#     if request.user.is_authenticated:
#       print('auth')
#       custom_user = CustomUser.objects.get(pk=request.user.id)
#       print(custom_user)
#       context['user'] = custom_user
#       print(request.user.id)
#     else:
#       return redirect('login')  
#     return render(request, 'myfoodgroups.html', context=context)

#   elif request.method == 'POST':
    
#     form = MyfoodgroupsForm(request.POST)
#     if form.is_valid():
     
#       form.save()
#       return redirect('myfitness')  
#     else:
#       context['form'] = form
#       return render(request, 'myfoodgroups.html', context=context)

def SignUpView(request):
  form_class = CustomUserCreationForm 
  success_url = reverse_lazy('login') 
  form=CustomUserCreationForm(request.POST or None)
  if form.is_valid():
    print('valid form')
    obj = form.save(commit=False)  
    obj.user_id=(request.user.id)
    obj.save()
    return redirect('login') 
  else:
     print(form.errors.as_data()) 
  context={'form':form}
  return render(request, 'signup.html', context=context)
  template_name = 'signup.html'
  return render(request, 'signup.html', {'alert_flag': True})

# def login_view(request):
#     if request.method == 'POST':
#         # Handle form submission and login logic
#         # ...
#         login(request, user)
#         return redirect('user_list.html')  # Redirect to the desired page
#     else:
#         form = LoginForm()  # Your custom login form
#         return render(request, 'login.html', {'form': form})  

class HomePageView(TemplateView):
 template_name = 'top3health-bootstrap.html'

# def staff_dashboard(request):
#     # ... (your dashboard logic)
#     return render(request, 'staff_dashboard.html', )
#     context: {'form':form}


def staff_register(request):
    if request.method == 'POST':
        form = StaffRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Don't call login(request, user) here
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = StaffRegistrationForm()  # Pre-populate if needed
    return render(request, 'staff_registration.html', {'form': form})
     
        
def customroleView(request):
    print(request)
    if request.user.is_authenticated:
        print(request.user)
        print(request.user.role)
        try:
            print(request.user.role)
            urole = request.user.role
            print(urole)
            if urole == 'dietician':
                
                return redirect('list_users')
            elif urole == 'user':
                return redirect('landing')
        except urole.DoesNotExist:
            # Handle case where CustomRole doesn't exist
            return render(request, 'error_page.html')
    else:
        return render(request, 'login.html')        
        
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class LandingView(TemplateView):
  success_url = reverse_lazy('landing')
  template_name = 'landing-bootstrap.html'
  context={"user":User}
  #pass goals into context

def DailylogView(request):
  form=MydailylogForm(request.POST or None)
  if form.is_valid():
    obj = form.save(commit=False)
    print(request.user.id)
    # print(obj.user.id)
    study = Study.objects.all()
    print(f"study: {study.customuser.id}")
    obj.customuser_id=(request.user.id)
    obj.save()
    
    # print (Customuser.Regular_or_Study_Mode)
    return redirect('goals')
     
  print(form.errors)
  
  context = {
         'form': form,
          'study': Study,
     }
  template_name = 'food_log2.html'
  return render(request, 'food_log2.html', context=context)


def my_view(request):
    study = Study.objects.get.all()
    mode = Study.objects.get(mode)  
    print("mode")
    print(mode)

    context = {
        'study': study,
        'mode': mode,
    }

    return render(request, 'food_log2.html', context) 


def BeginpageView(request):
  form=BeginpageForm(request.POST or None)
  if form.is_valid():
    obj = form.save(commit=False)
    print(request.user.id)
    # print(obj.user.id)
    obj.customuser_id=(request.user.id)
    obj.save()
    
    # print (Customuser.Regular_or_Study_Mode)
    return redirect('/landing')
     
  print(form.errors)
  context={'form':form}
  template_name = 'begindate.html'
  return render(request, 'begindate.html', context=context)    

def MysuggestionsView(request):
   return render(request, 'weekly_suggestions.html')


# works with onetoone, not foreignkey

# def list_users(request):
#     users = CustomUser.objects.exclude(Q(role='dietician') | Q(is_superuser=True))
#     user_data = []

#     # Print users once outside the loop (optional)
#     # print(users)  # Uncomment if you need to see the complete list

#     for user in users:
#         try:
#             profile = user.myprofile
#             gender = profile.Gender
#             height_ft = profile.Height_ft
#             height_in = profile.Height_in
#             weight = profile.Weight_in_pounds
#             calories_in = profile.Calories_intake
#             calories_burned = profile.Calories_burned
#             protein = profile.Protein_intake

#             # Handle missing Minorsym data (optional, uncomment if needed)
#             # try:
#             #     minorsym = user.minorsym_set.first()
#             #     minorsym_data = {'fatigue': minorsym.Fatigue, ...}
#             # except Minorsym.DoesNotExist:
#             #     minorsym_data = None

#             user_data.append({
#                 'userid': user.id,
#                 'username': user.username,
#                 'first_name': user.first_name,
#                 'gender': gender,
#                 'height_ft': height_ft,
#                 'height_in': height_in,
#                 'weight': weight,
#                 'calories_in': calories_in,
#                 'calories_burned': calories_burned,
#                 'protein': protein,

#                 # Include minorsym data if implemented (uncomment)
#                 # 'minorsym': minorsym_data,
#             })
#         except MyProfile.DoesNotExist:
#             # Handle missing profile case (you might want to log this)
#             pass  # Add appropriate handling for missing profile

#     return render(request, 'user_list.html', {'users': user_data})

# from django.db.models import Q

# works with both foreign key and onetoone

# def list_users(request):
#     users = CustomUser.objects.exclude(Q(role='dietician') | Q(is_superuser=True))
#     user_data = []

#     for user in users:
#         # try:
#             # Handle both one-to-one and foreign key relationships
#             # if hasattr(user, 'myprofile'):
#             #     profile = user.myprofile  # One-to-one case
#             #     minorsym = user.minorsym
#             # else:
#             #     # Foreign key case: Fetch the most recent profile
#             #     profile = user.myprofile_set.order_by('-id').first()

#              try:
#                   print(users)
#                   profile = user.myprofile
#                   print (profile)
#                   minorsym = user.minorsym 
#                   print(minorsym)

#                   gender = profile.Gender
#                   height_ft = profile.Height_ft
#                   height_in = profile.Height_in
#                   weight = profile.Weight_in_pounds
#                   calories_in = profile.Calories_intake
#                   calories_burned = profile.Calories_burned
#                   protein = profile.Protein_intake

#                   user_data.append({
#                   'userid': user.id,
#                   'username': user.username,
#                   'first_name': user.first_name,
#                   'gender': gender,
#                   'height_ft': height_ft,
#                   'height_in': height_in,
#                   'weight': weight,
#                   'calories_in': calories_in,
#                   'calories_burned': calories_burned,
#                   'protein': protein,
#             })
#              except (MyProfile.DoesNotExist, AttributeError):
#             # Handle both missing profile and potential model attribute errors
#             # (e.g., if 'myprofile' doesn't exist on the user model)
#             # You might want to log this or handle it differently
#               pass

#     return render(request, 'user_list.html', {'users': user_data})


def list_users(request):
    users = CustomUser.objects.exclude(Q(role='Dietician') | Q(is_superuser=True))
    
    user_data = []
    for user in users:
        print(user)
        print(user.role)
        latest_healthsym = user.healthsym_set.order_by('-created_at').first()
        if latest_healthsym:
         print("Latest healthsym found for user:", user.id)
        else:
         print("No latest healthsym found for user:", user.id)
        # print(latest_healthsym)
        
        try:
            minor1 = latest_healthsym.Minor1 if latest_healthsym else None
            print(minor1)
            minor2 = latest_healthsym.Minor2 if latest_healthsym else None
            minor3 = latest_healthsym.Minor3 if latest_healthsym else None
            minor4 = latest_healthsym.Minor4 if latest_healthsym else None
            minor5 = latest_healthsym.Minor5 if latest_healthsym else None

            major1 = latest_healthsym.Major1 if latest_healthsym else None
            major2 = latest_healthsym.Major2 if latest_healthsym else None
            major3 = latest_healthsym.Major3 if latest_healthsym else None
            major4 = latest_healthsym.Major4 if latest_healthsym else None
            major5 = latest_healthsym.Major5 if latest_healthsym else None

            

        except Healthsym.DoesNotExist:
            # Set all fields to None if Healthsym doesn't exist
            minor1 = None
            minor2 = None
            minor3 = None
            minor4 = None
            minor5 = None
            major1 = None
            major2 = None
            major3 = None
            major4 = None
            major5 = None

        user_data.append({
            'userid': user.id,
            'username': user.username,
            'first_name': user.first_name,

            'minor1': minor1,
            'minor2': minor2,
            'minor3': minor3,
            'minor4': minor4,
            'minor5': minor5,

            'major1': major1,
            'major2': major2,
            'major3': major3,
            'major4': major4,
            'major5': major5,
        })
        print("User data:", user_data)
         
        form = DieticiannoteForm(request.POST or None)
        if form.is_valid():
            obj = form.save(commit=False)
            print(request.user.id)
            
                    
        context={'users': user_data,
                
                'healthsym':Healthsym,
                'minor1':minor1}
        template_name = 'user_list.html'
    
    return render(request, 'user_list.html', context=context)
    # for user in users:
      #  for field_name in user._meta.fields:
      #       field_value = getattr(user, field_name.name)
      #       print(f"{field_name.name}: {field_value}")

def GoalsView(request):
  form=GoalsForm(request.POST or None)
  if form.is_valid():
    obj = form.save(commit=False)
    print(request.user.id)
    # print(obj.user.id)
    obj.customuser_id=(request.user.id)
    obj.save()
    
    # print (Customuser.Regular_or_Study_Mode)
    return redirect('/myprofile')
     
  print(form.errors)
  context={'form':form}
  template_name = 'goals-bootstrap.html'
  return render(request, 'goals-bootstrap.html', context=context)

@login_required
def GoalsUpdateView(request):
    current_user = request.user

    if request.method == 'POST':
        form = GoalsForm(request.POST)
        if form.is_valid():
            goals = form.save(commit=False)
            goals.customuser = current_user
            goals.created_at = timezone.now()
            goals.save()
            return redirect('landing')
    else:
        goals = Goals.objects.filter(customuser=current_user).order_by('-created_at').first()
        form = GoalsForm(instance=goals)

    context = {
        'form': form,
        'goals': goals,
    }

    return render(request, 'goals-update-bootstrap.html', context)


def MyProfileView(request):
  form=ProfileForm(request.POST or None)
  if form.is_valid():
    
    obj = form.save(commit=False)
    obj.customuser_id=(request.user.id)
    obj.save()
    return redirect('/healthscreening')
  print(form.errors)
  # form= ProfileForm()
  context={'form':form}
  template_name = 'profile-bootstrap.html'
  return render(request, 'profile-bootstrap.html', context=context)


# def ProfileUpdateView(request):
#     current_user = CustomUser.objects.get(id=request.user.id)  
    
#     form=ProfileForm(request.POST or None, instance=current_user)
#     form_ver = ProfileverForm(request.POST or None, instance=current_user)
#     myprofile = MyProfile.objects.all().get(customuser=request.user.id)
   
#     if form_ver.is_valid():
      
#       obj = form_ver.save(commit=False)
#       obj=form_ver.cleaned_data
      
#       New_profile=MyProfile_ver(customuser=request.user, 
#       Height_ft=myprofile.Height_ft,
#       Height_in=myprofile.Height_in,
#       Weight_in_pounds=myprofile.Weight_in_pounds,
#       Gender=myprofile.Gender,
#       Calories_intake=myprofile.Calories_intake,
#       Calories_burned=myprofile.Calories_burned,
#       Protein_intake=myprofile.Protein_intake,
#       Carbs_intake=myprofile.Carbs_intake,
#       Water_intake=myprofile.Water_intake,
#       Race=myprofile.Race,
#       Ethnicity=myprofile.Ethnicity,
#       Stress_level=myprofile.Stress_level,
#       Sleep_quality=myprofile.Sleep_quality,
#       Blood_type=myprofile.Blood_type)
#       print(Myhealthstatus.objects.all())
      
#       New_profile.save()
      
#     else:
#       print(form.errors)
      
#     if form.is_valid():
    
#       obj=form.save(commit=False)
#       obj=form.cleaned_data          

#       myprofile.Height_ft=obj['Height_ft']
#       myprofile.Height_in=obj['Height_in']
#       myprofile.Weight_in_pounds=obj['Weight_in_pounds']
#       myprofile.Gender=obj['Gender']
#       myprofile.Calories_intake=obj['Calories_intake']
#       myprofile.Calories_burned=obj['Calories_burned']
#       myprofile.Protein_intake=obj['Protein_intake']
#       myprofile.Carbs_intake=obj['Carbs_intake']
#       myprofile.Water_intake=obj['Water_intake']
#       myprofile.Race=obj['Race']
#       myprofile.Ethnicity=obj['Ethnicity']
#       myprofile.Stress_level=obj['Stress_level']
#       myprofile.Sleep_quality=obj['Sleep_quality']
#       myprofile.Blood_type=obj['Blood_type']

#       myprofile.save()
#       return redirect('landing')


#     context={
#          'form':form,
#          'myprofile':myprofile,
#         # 'myprofile_ver':Myprofile_ver
#       }  
 
#     return render(request, 'myprofileUpdate.html', context=context) 


def MyHealthscreeningView(request):
  form=MyhealthscreeningForm(request.POST or None)
  if form.is_valid():
    print(request.user.id)
    obj = form.save(commit=False)
    obj.customuser_id=(request.user.id)
    obj.save()
    return redirect('/minorsym')
  print(form.errors)
  # form= ProfileForm()
  context={'form':form}
  template_name = 'healthscreening.html'
  return render(request, 'healthscreening.html', context=context)


@login_required
def HealthscreeningUpdateView(request):
    current_user = request.user

    if request.method == 'POST':
        form = MyhealthscreeningForm(request.POST)
        if form.is_valid():
            myhealthscreening = form.save(commit=False)
            myhealthscreening.customuser = current_user
            myhealthscreening.created_at = timezone.now()
            myhealthscreening.save()
            return redirect('landing')
    else:
        myhealthscreening = Myhealthscreening.objects.filter(customuser=current_user).order_by('-created_at').first()
        form = MyhealthscreeningForm(instance=myhealthscreening)

    context = {
        'form': form,
        'myhealthscreening': myhealthscreening,
    }

    return render(request, 'healthscreeningupdate.html', context)

# def HealthscreeningUpdateView(request):
#     current_user = CustomUser.objects.get(pk=request.user.id)
   
#     form = MyhealthscreeningForm(request.POST or None, instance=current_user)
#     form_ver = MyhealthscreeningverForm(request.POST or None, instance=current_user)
#     myhealthscreening = Myhealthscreening.objects.all().get(customuser=request.user.id)

#     if form_ver.is_valid():
#       print('ver form valid') 
#       # print(goals.customuser)
#       obj=form_ver.save(commit=False)
#       obj=form_ver.cleaned_data
#       New_myhealthscreening=Myhealthscreening_ver(customuser=request.user,
#       Blood_glucose=myhealthscreening.Blood_glucose,
#       A1C =  myhealthscreening.A1C,
#       BP_systolic=myhealthscreenig.BP_systolic,
#       BP_diastolic=myhealthscreening.BP_diastolic,
#       Total_Cholesterol=myhealthscreening.Total_Cholesterol,
#       HDL=myhealthscreening.HDL,
#       LDL=myhealthscreening.LDL,
#       Triglycerides=myhealthscreening.Triglycerides,
#       Smoker=myhealthscreening.Smoker,
#       Blood_type=myhealthscreening.Blood_type,

#       Dental_checkups=myhealthscreening.Dental_checkups,
#       Dental_cleanings=myhealthscreening.Dental_cleanings,

#       Screen_date=myhealthscreening.Screen_date
#       )
      
#       New_myhealthscreening.save()

#     else:
#       print(form.errors)  

#     if form.is_valid():
#       print('main form valid') 
#       obj=form.save(commit=False)
#       obj=form.cleaned_data
      
#       myhealthscreening.Blood_glucose=obj['Blood_glucose']
#       myhealthscreening.A1C=obj['A1C']
#       myhealthscreening.BP_systolic=obj['BP_systolic']
#       myhealthscreening.BP_diastolic=obj['BP_diastolic']
#       myhealthscreening.Total_Cholesterol=obj['Total_Cholesterol']
#       myhealthscreening.HDL=obj['HDL']
#       myhealthscreening.LDL=obj['LDL']
#       myhealthscreening.Triglycerides=obj['Triglycerides']
#       myhealthscreening.Smoker=obj['Smoker']
#       myhealthscreening.Blood_type=obj['Blood_type']
     
#       myhealthscreening.Dental_checkups=obj['Dental_checkups']
#       myhealthscreening.Dental_checkups=obj['Dental_cleanings']
#       myhealthscreening.Screen_date=obj['Screen_date']

#       myhealthscreening.save()

#       return redirect('landing')
     
#     context={
#           'form':form,
#           'myhealthscreening_ver':Myhealthscreening_ver,
#           'myhealthscreening':myhealthscreening,
#         }

#     return render(request, 'healthscreeningupdate.html', context=context)

# orig view function, modified after cleaned data
def MinorsymView(request):
  form=HealthsymForm(request.POST or None)
  if form.is_valid():
    
    obj = form.save(commit=False)
    obj.customuser_id=(request.user.id)
    obj.save()
    return redirect('mybreakfastdesign')
  print(form.errors)
 
  context={'form':form}
  template_name = 'minorsymptoms-bootstrap.html'
  return render(request, 'minorsymptoms-bootstrap.html', context=context)


# def MinorsymView(request):
#   form = MinorsymForm(request.POST or None)  # Create the form with POST data

#   if form.is_valid():
#     # Access the cleaned data directly from the form
#     cleaned_data = form.cleaned_data
#     print(cleaned_data)

#     # Create a new instance of your model
#     obj = Minorsym(**cleaned_data)

#     # Optionally set additional fields outside the form
#     obj.customuser_id = request.user.id

#     # Save the model instance
#     obj.save()

#     # Redirect to the desired page
#     return redirect('/majorsym')

#   # Handle validation errors
#   print(form.errors)

#   # Render the template with the form
#   context = {'form': form}
#   template_name = 'minorsymptoms-bootstrap.html'
#   return render(request, template_name, context=context)

@login_required
def MinorsymUpdateView(request):
    current_user = request.user

    if request.method == 'POST':
        form = HealthsymForm(request.POST)
        if form.is_valid():
            minorsym = form.save(commit=False)
            minorsym.customuser = current_user
            minorsym.created_at = timezone.now()
            minorsym.save()
            
            return redirect('/landing')
    else:
        print("error in minor form?")
        minorsym = Minorsym.objects.filter(customuser=current_user).order_by('-created_at').first()
        form = HealthsymForm(instance=minorsym)

    context = {
        'form': form,
        'minorsym': minorsym,
    }
    # template_name = 'minorsymupdate.html'
    return render(request, 'minorsymupdate.html', context)


def MyexpensesView(request):
  form=MyexpensesForm(request.POST or None)  
  if form.is_valid():
    print('Valid')
    obj = form.save(commit=False)
    obj.customuser_id=(request.user.id)
    obj.save()
    return redirect('/landing') 
  else:
     print(form.errors)   
  context={'form':form}
  template_name = 'myexpenses.html'
  return render(request, 'myexpenses.html', context=context)
  print(request.user)
  

def ExpensesUpdateView(request):
    current_user = CustomUser.objects.get(pk=request.user.id)
    form = MyexpensesForm(request.POST or None, instance=current_user)
    form_ver = MyexpensesverForm(request.POST or None, instance=current_user)
    myexpenses = Myexpenses.objects.all().get(customuser=request.user.id)

    if form_ver.is_valid():
        print(request.user) 
        obj=form_ver.save(commit=False)
        obj=form_ver.cleaned_data
        New_expenses=Myexpenses_ver(customuser=request.user,
        family_eatout_count=myexpenses.family_eatout_count,
        weekly_eatout_cost=myexpenses.weekly_eatout_cost,
        family_grocery_count=myexpenses.family_grocery_count,
        weekly_grocery_cost=myexpenses.weekly_grocery_cost,
        Misc_expense_member=myexpenses.Misc_expense_member,
        Misc_expenses=myexpenses.Misc_expenses,
        family_premium_count=myexpenses.family_premium_count,
        insurance_premium=myexpenses.insurance_premium,
        members_for_office_visit=myexpenses.members_for_office_visit,
        office_visit_cost=myexpenses.office_visit_cost,
        members_for_prescriptions=myexpenses.members_for_prescriptions,
        prescription_cost=myexpenses.prescription_cost,
        members_for_oop=myexpenses.members_for_oop,
        oop_cost=myexpenses.oop_cost,
        members_for_gym=myexpenses.members_for_gym,
        gym_cost=myexpenses.gym_cost)

        New_expenses.save()
    else:
      print(form.errors)    
    if form.is_valid():
      obj=form.save(commit=False)
      obj=form.cleaned_data
      myexpenses.family_eatout_count=obj['family_eatout_count']
      myexpenses.weekly_eatout_cost=obj['weekly_eatout_cost']
      myexpenses.family_grocery_count=obj['family_grocery_count']
      myexpenses.weekly_grocery_cost=obj['weekly_grocery_cost']
      myexpenses.Misc_expense_member=obj['Misc_expense_member']
      myexpenses.Misc_expenses=obj['Misc_expenses']
      myexpenses.family_premium_count=obj['family_premium_count']
      myexpenses.insurance_premium=obj['insurance_premium']
      myexpenses.members_for_office_visit=obj['members_for_office_visit']
      myexpenses.office_visit_cost=obj['office_visit_cost']
      myexpenses.members_for_prescriptions=obj['members_for_prescriptions']
      myexpenses.prescription_cost=obj['prescription_cost']
      myexpenses.members_for_oop=obj['members_for_oop']
      myexpenses.oop_cost=obj['oop_cost']
      myexpenses.members_for_gym=obj['members_for_gym']
      myexpenses.gym_cost=obj['gym_cost']

      myexpenses.save()
            
      return redirect('landing')

    context={
          'form':form,
          'myexpenses_ver':Myexpenses_ver,
          'myexpenses':myexpenses,
        }  
        
    return render(request, 'myexpensesupdate.html', context=context)        

def MyhabitsView(request):
  form=MyhabitsForm(request.POST or None)  
  if form.is_valid():
    print('Valid')
    obj = form.save(commit=False)
    obj.customuser_id=(request.user.id)
    obj.save()
    return redirect('/landing') 
  else:
     print(form.errors)   
  context={'form':form}
  template_name = 'myhabits.html'
  return render(request, 'myhabits.html', context=context)
  print(request.user)    


def MyfitnessView(request):
  form=MyfitnessForm(request.POST or None)  
  if form.is_valid():
    obj = form.save(commit=False)
    obj.customuser_id=(request.user.id)
    obj.save()
    return redirect('minorsym') 
  context={'form':form}
  # print("form : "+str(form))
  template_name = 'myfitness-bootstrap.html'
  return render(request, 'myfitness-bootstrap.html', context=context)
  # return render(request, 'myfitness-bootstrap.html', {'alert_flag': True})
  print(request.user)

# def MyfoodgroupsView(request):
#   form=MyfoodgroupsForm(request.POST or None) 
#   if form.is_valid():
#     obj = form.save(commit=False)
#     obj.customuser_id=(request.user.id)
#     print('ooo')
#     print(request.user)
#     # print(request.user.id)
#     obj.save()
#     return redirect('/myfitness')  
#   print(form.errors)
#   context={'form':form}
#   template_name = 'myfoodgroups.html'
#   return render(request, 'myfoodgroups.html', context=context)
#   # return render(request, 'myfoodgroups.html', {'alert_flag': True})
#   print(request.user)  

# def MyfoodgroupsView(request):
#   if request.user.is_authenticated:
#     form=MyfoodgroupsForm(request.POST or None) 
#     if form.is_valid():
#       obj = form.save(commit=False)
#       obj.customuser = request.user  # Directly assign the user object
#       print('ooo')
#       print(request.user)
#       obj.save()
#       return redirect('/myfitness')  
#   else:
#       # Handle unauthenticated user case (e.g., redirect to login)
#       return redirect('/login')  # Redirect to login page

#   print(form.errors)
#   context={'form':form}
#   template_name = 'myfoodgroups.html'
#   return render(request, 'myfoodgroups.html', context=context)  

def MyfoodgroupsverView(request):
    current_user = CustomUser.objects.get(pk=request.user.id)
    form = MyfoodgroupsForm(request.POST or None, instance=current_user)
    form_ver = MyfoodgroupsverForm(request.POST or None, instance=current_user)
    myfoods = Myfoodgroups.objects.all().get(customuser=request.user.id)
    if form_ver.is_valid():
        print('ver form valid') 
        obj=form_ver.save(commit=False)
        obj=form_ver.cleaned_data

        new_myfoods=Myfoodgroupsver(customuser=request.user,

        Green_veggies=myfoods.Green_veggies, 
        Red_Orange_veggies=myfoods.Red_Orange_veggies,
        Other_veggies=myfoods.Other_veggies,
        Fruits_Berries=myfoods.Fruits_Berries,
        Protein=myfoods.Protein,
        Grains=myfoods.Grains,
        Dairy=myfooods.Dairy,   
        Herbs_Spices=myfoods.Spices,
        )
        new_myfoods.save()

    else:
      print(form.errors)

      if form.is_valid():
        print('main form valid')
        obj=form.save(commit=False)
        obj=form.cleaned_data    

        myfoods.Green_veggies=obj['Green_veggies']
        myfoods.Red_Orange_veggies=obj['Red_Orange_veggies']
        myfoods.Other_veggies=obj['Other_veggies']
        myfoods.Fruits=obj['Fruits_Berries']
        myfoods.Protein=obj['Protein']
        myfoods.Grains=obj['Grains']
        myfoods.Dairy=obj['Dairy']
        myfoods.Spices=obj['Herbs_Spices']

        myfoods.save()
        return redirect('landing')
    context={
          'form':form,
          'myfoodgroups':Myfoodgroups,
          'myfoods':myfoods}
          #'new_myfoods':new_myfoods,}
        
    # template_name = 'myexpensesupdate.html'
    return render(request, 'myfoodgroupsupdate.html', context=context)  


def MyfastfoodsView(request):
  form=MyfastfoodsForm(request.POST or None) 
  if form.is_valid():
    obj = form.save(commit=False)
    obj.customuser_id=(request.user.id)
    obj.save()
    return redirect('/myfoodsuggestions')
  else:
     print(form.errors)     
  context={'form':form}
  template_name = 'myfastfoods.html'
  return render(request, 'myfastfoods.html', context=context)
  print(request.user)  


def MyfastfoodsUpdateView(request):
    current_user = CustomUser.objects.get(id=request.user.id)  
    
    form=MyfastfoodsForm(request.POST or None, instance=current_user)
    form_ver = MyfastfoodsverForm(request.POST or None, instance=current_user)
    fastfoods = Myfastfoods.objects.all().get(customuser=request.user.id)
   
    if form_ver.is_valid():
      
      obj = form_ver.save(commit=False)
      obj=form_ver.cleaned_data
      
      New_fastfoods=Myfastfoods_ver(customuser=request.user,   
      Bacon=fastfoods.Bacon,
      Burgers=fastfoods.Burgers,
      Cookies=fastfoods.Cookies,
      Cereals=fastfoods.Cereals,
      Frozen_pizza=fastfoods.Frozen_pizza,
      Ice_cream=fastfoods.Ice_cream,
      
      Pancakes=fastfoods.Pancakes,
      Fried_foods=fastfoods.Fried_foods,
      Popcorn=fastfoods.Popcorn,
      Frozen_meals=fastfoods.Frozen_meals,
      
      Soft_drinks=fastfoods.Soft_drinks,
      
      Milk_shakes=fastfoods.Milk_shakes,
      Potato_chips=fastfoods.Potato_chips,
      French_fries=fastfoods.French_fries,
      
      )
      
      New_fastfoods.save()
      
    else:
      print(form.errors)
      
    if form.is_valid():
    
      obj=form.save(commit=False)
      obj=form.cleaned_data          

      fastfoods.Bacon=obj['Bacon']
      fastfoods.Burgers=obj['Burgers']
      
      fastfoods.Cookies=obj['Cookies']
      fastfoods.Pancakes=obj['Pancakes']
      fastfoods.Cereals=obj['Cereals']
      
      fastfoods.Frozen_pizza=obj['Frozen_pizza']
      fastfoods.Ice_cream=obj['Ice_cream']
      
      fastfoods.Fried_foods=obj['Fried_foods']
      fastfoods.Popcorn=obj['Popcorn']
      
      fastfoods.Frozen_meals=obj['Frozen_meals']
      fastfoods.Soft_drinks=obj['Soft_drinks']
      
      fastfoods.Milk_shakes=obj['Milk_shakes']
      fastfoods.Potato_chips=obj['Potato_chips']
      
      fastfoods.French_fries=obj['French_fries']
      print(fastfoods.French_fries)
    
      fastfoods.save()
      return redirect('landing')


    context={
         'form':form,
         'fastfoods':fastfoods,
           'Myfastfoods_ver':Myfastfoods_ver,
         
      }  
 
    return render(request, 'myfastfoodsupdate.html', context=context)   


def MyfoodsuggestionsView(request):
  form=MyfoodsuggestionsForm(request.POST or None) 
  if form.is_valid():
    obj = form.save(commit=False)
    obj.customuser_id=(request.user.id)
    obj.save()
    return redirect('/myallergicfoods')
  else:
     print(form.errors)     
  context={'form':form}
  template_name = 'myfoodsuggestions.html'
  return render(request, 'myfoodsuggestions.html', context=context)
  print(request.user)      

def MyallergicfoodsView(request):
  form=MyallergicfoodsForm(request.POST or None) 
  if form.is_valid():
    obj = form.save(commit=False)
    obj.customuser_id=(request.user.id)
    obj.save()
    return redirect('/supplements') 
  else:
     print(form.errors)  
  context={'form':form}
  template_name = 'myallergicfoods.html'
  return render(request, 'myallergicfoods.html', context=context)
  # return render(request, 'myallergicfoods.html', {'alert_flag': True})
  print(request.user)    

# def MytrigfoodsView(request):
#   form=MytrigfoodsForm(request.POST or None) 
#   if form.is_valid():
#     obj = form.save(commit=False)
#     obj.customuser_id=(request.user.id)
#     obj.save()
#     return redirect('/mytypbreakfast.html') 
#   else:
#      print(form.errors)  
#   context={'form':form}
#   template_name = 'mytriggerfoods.html'
#   return render(request, 'mytriggerfoods.html', context=context)
#   # return render(request, 'myallergicfoods.html', {'alert_flag': True})
#   print(request.user)  

def MyallergicfoodsUpdateView(request):
    current_user = CustomUser.objects.get(id=request.user.id)  
    
    form=MyallergicfoodsForm(request.POST or None, instance=current_user)
    form_ver = MyallergicfoodsverForm(request.POST or None, instance=current_user)
    myallergies = Myallergicfoods.objects.all().get(customuser=request.user.id)
    
  
    if form_ver.is_valid():
      
      obj = form_ver.save(commit=False)
      obj=form_ver.cleaned_data
      
      New_allergies=Myallergicfoods_ver(customuser=request.user,     
      
      allergicFood1=myallergies.Regular_Milk,
      Regular_Yogurt=myallergies.Regular_Yogurt,
      Greek_Yogurt=myallergies.Greek_Yogurt,
      Lactose_free_Milk=myallergies.Lactose_free_Milk,
      Peanuts=myallergies.Peanuts,
      Walnuts=myallergies.Walnuts,
      Pecans=myallergies.Pecans,
      Shell_fish=myallergies.Shell_fish,
      Fish=myallergies.Fish,
      Soy=myallergies.Soy,
      Eggs=myallergies.Eggs,
      Sesame=myallergies.Sesame,
      Wheat=myallergies.Wheat,
      Gluten_free_foods=myallergies.Gluten_free_foods,

      Main_Food_1=myallergies.Main_Food_1,
      Main_Food_2=myallergies.Main_Food_2,
      Main_Food_3=myallergies.Main_Food_3,


      Food_substitute_1=myallergies.Food_substitute_1,
      Food_substitute_2=myallergies.Food_substitute_2,
      Food_substitute_3=myallergies.Food_substitute_3,

      )
      
      New_allergies.save()
      
    else:
      print(form.errors)
      
    if form.is_valid():
    
      obj=form.save(commit=False)
      obj=form.cleaned_data          
     
      myallergies.Regular_Milk=obj['Regular_Milk']
      myallergies.Regular_Yogurt=obj['Regular_Yogurt']
      myallergies.Greek_Yogurt=obj['Greek_Yogurt']
      myallergies.Lactose_free_Milk=obj['Lactose_free_Milk']
      myallergies.Peanuts=obj['Peanuts']
      myallergies.Walnuts=obj['Walnuts']
      myallergies.Pecans=obj['Pecans']
      myallergies.Shell_fish=obj['Shell_fish']
      myallergies.Fish=obj['Fish']
      myallergies.Eggs=obj['Eggs']
      myallergies.Soy=obj['Soy']
      myallergies.Sesame=obj['Sesame']
      myallergies.Wheat=obj['Wheat']
      myallergies.Gluten_free_foods=obj['Gluten_free_foods']
      myallergies.Main_Food_1=obj['Main_Food_1']
      myallergies.Main_Food_1=obj['Main_Food_2']
      myallergies.Main_Food_1=obj['Main_Food_3']

      myallergies.Food_substitute_1=obj['Food_substitute_1']
      myallergies.Food_substitute_2=obj['Food_substitute_2']
      myallergies.Food_substitute_3=obj['Food_substitute_3']
      
      myallergies.save()
      return redirect('landing')

    context={
         'form':form,
         'myallergies':myallergies,
         'myallergicfoods_ver':myallergicfoods_ver,
      }  
 
    return render(request, 'myallergicfoodsUpdate.html', context=context)


def MysettingsView(request):
   return render(request, 'settings.html')

def MyprofileandgoalsView(request):   
   return render(request, 'myprofileandgoals.html')


@login_required
def SupplementsUpdateView(request):
    current_user = request.user

    if request.method == 'POST':
        form = SupplementsForm(request.POST)
        if form.is_valid():
            supplements = form.save(commit=False)
            supplements.customuser = current_user
            supplements.created_at = timezone.now()
            supplements.save()
            return redirect('landing')
    else:
        supplements = Supplements.objects.filter(customuser=current_user).order_by('-created_at').first()
        form = SupplementsForm(instance=supplements)

    context = {
        'form': form,
        'supplements': supplements,
    }

    return render(request, 'supplements_update.html', context)

# def SupplementsUpdateView(request):
#     current_user = CustomUser.objects.get(pk=request.user.id)
   
#     form = SupplementsForm(request.POST or None, instance=current_user)
#     form_ver = SupplementsverForm(request.POST or None, instance=current_user)
#     supplements = Supplements.objects.all().get(customuser=request.user.id)

#     if form_ver.is_valid():
#       print('ver form valid') 
#       print(supplements.customuser)
#       obj=form_ver.save(commit=False)
#       obj=form_ver.cleaned_data
#       New_supplements=Supplements_ver(customuser=request.user,
#       Supplement_1=supplements.Supplement_1, 
#       Supplement_2=supplements.Supplement_2, 
#       Supplement_3=supplements.Supplement_3, 
#       Supplement_4=supplements.Supplement_4, 
#       Supplement_5=supplements.Supplement_5, 
#       Supplement_6=supplements.Supplement_6, 
#       Supplement_7=supplements.Supplement_7, 
#       Supplement_8=supplements.Supplement_8, 
#       Supplement_9=supplements.Supplement_9, 
#       Supplement_10=supplements.Supplement_10)

#       print('valid')
#       New_supplements.save()

#     else:
#       print(form.errors)  

#     if form.is_valid():
#       print('main form valid') 
#       obj=form.save(commit=False)
#       obj=form.cleaned_data
#       print('valid 2')
#       supplements.Supplement_1=obj['Supplement_1']
#       supplements.Supplement_2=obj['Supplement_2']
#       supplements.Supplement_3=obj['Supplement_3']
#       supplements.Supplement_4=obj['Supplement_4']
#       supplements.Supplement_5=obj['Supplement_5']
#       supplements.Supplement_6=obj['Supplement_6']
#       supplements.Supplement_7=obj['Supplement_7']
#       supplements.Supplement_8=obj['Supplement_8']
#       supplements.Supplement_9=obj['Supplement_9']
#       supplements.Supplement_10=obj['Supplement_10']
      
#       print('form passed')
#       supplements.save()

#       return redirect('landing')
     
#     context={
#           'form':form,
#           'supplements_ver':Supplements_ver,
#           'supplements':supplements,
#         }

#     return render(request, 'supplements_update.html', context=context)   

def MybreakfastdesignView(request):
  form=Mytypmeals1Form(request.POST or None)  
  if form.is_valid():
    obj = form.save(commit=False)
    obj.customuser_id=(request.user.id)
    obj.save()
    return redirect('/supplements')
  else:
    print(form.errors)  
  context={'form':form}
  template_name = 'mybreakfastdesign.html'
  return render(request, 'mybreakfastdesign.html', context=context)
  print(request.user)

def MylunchdesignView(request):
  form=Mytypmeals1Form(request.POST or None)  
  if form.is_valid():
    obj = form.save(commit=False)
    obj.customuser_id=(request.user.id)
    obj.save()
    return redirect('/mydinnerdesign')
  else:
    print(form.errors)  
  context={'form':form}
  template_name = 'mylunchdesign.html'
  return render(request, 'mylunchdesign.html', context=context)
  print(request.user)

def MydinnerdesignView(request):
  form=Mytypmeals1Form(request.POST or None)  
  if form.is_valid():
    obj = form.save(commit=False)
    obj.customuser_id=(request.user.id)
    obj.save()
    return redirect('/supplements')
  else:
    print(form.errors)  
  context={'form':form}
  template_name = 'mydinnerdesign.html'
  return render(request, 'mydinnerdesign.html', context=context)
  print(request.user)

def Mytypmeals1View(request):
  form=Mytypmeals1Form(request.POST or None)  
  if form.is_valid():
    obj = form.save(commit=False)
    obj.customuser_id=(request.user.id)
    obj.save()
    return redirect('/supplements')
  else:
    print(form.errors)  
  context={'form':form}
  template_name = 'mytypicalmeals1.html'
  return render(request, 'mytypicalmeals1.html', context=context)
  print(request.user)


def Mytypmeals2View(request):
  form=Mytypmeals2Form(request.POST or None)  
  if form.is_valid():
    obj = form.save(commit=False)
    obj.customuser_id=(request.user.id)
    obj.save()
    return redirect('supplements')
  else:
    print(form.errors)  
  context={'form':form}
  template_name = 'mytypicalmeals2.html'
  return render(request, 'mytypicalmeals2.html', context=context)
  print(request.user)
 


def MysupplementsView(request):
  form=SupplementsForm(request.POST or None)  
  if form.is_valid():
    print("Valid")
    print(request.user) 
    obj = form.save(commit=False)
    obj.customuser_id=(request.user.id)
    obj.save()
    return redirect('begindate')
  else:
   
    print(form.errors)   
 
  context={'form':form}
  return render(request, 'supplements.html', context=context)
  template_name = 'supplements.html'
  # return render(request, 'supplements.html', {'alert_flag': True})
  print(request.user) 



def MyfitnessUpdateView(request):
    current_user = CustomUser.objects.get(pk=request.user.id)
   
    form = MyfitnessForm(request.POST or None, instance=current_user)
    form_ver = MyfitnessverForm(request.POST or None, instance=current_user)
    myfit = Myfitness.objects.all().get(customuser=request.user.id)
    print(myfit)

    if form_ver.is_valid():
      print('ver form valid') 
      # print(myfitness.customuser)
      obj=form_ver.save(commit=False)
      obj=form_ver.cleaned_data
      New_fit=Myfitness_ver(customuser=request.user,
      
      Walking=myfit.Walking, 
      Walks_per_week=myfit.Walks_per_week,
      Include_Walks=myfit.Include_Walks,

      
      Jogging=myfit.Jogging, 
      Jogs_per_week=myfit.Jogs_per_week,
      Include_Jogging=myfit.Include_Jogging,
       
      Elliptic_Machine=myfit.Elliptic_Machine, 
      Elliptic_Machine_workouts_per_week=myfit.Elliptic_Machine_workouts_per_week, 
      Include_Elliptic=myfit.Include_Elliptic,


      Weight_lifting=myfit.Weight_lifting, 
      Weight_lifting_per_week=myfit.Weight_lifting_per_week, 
      Include_Weights=myfit.Include_Weights,

      
      Biking=myfit.Biking, 
      Bike_rides_per_week=myfit.Bike_rides_per_week,
      Include_Biking=myfit.Include_Biking,

       
      Zumba=myfit.Zumba,
      Zumba_workouts_per_week=myfit.Zumba_workouts_per_week,
      Include_Zumba=myfit.Include_Zumba,
      
      
      Swimming=myfit.Swimming, 
      Swimming_sessions_per_week=myfit.Swimming_sessions_per_week,
      Include_Swimming=myfit.Include_Swimming,

      
      Martial_arts=myfit.Martial_arts, 
      Martial_arts_practices_per_week=myfit.Martial_arts_practices_per_week,
      Include_Martialarts=myfit.Include_Martialarts, 
      
      # Bootcamp=myfit.Bootcamp, 
      # Bootcamp_workouts_per_week=myfit.Bootcamp_workouts_per_week, 
      
      # Taichi=myfit.Taichi, 
      # Taichi_practices_per_week=myfit.Taichi_practices_per_week,
       
      # Sports=myfit.Sports,
      # Sports_practices_per_week=myfit.Sports_practices_per_week,
      
      
      # Pilates=myfit.Pilates, 
      # Pilates_practices_per_week=myfit.Pilates_practices_per_week, 
      
      Yoga=myfit.Yoga, 
      Yoga_practices_per_week=myfit.Yoga_practices_per_week,
      Include_Yoga=myfit.Include_Yoga,
       
      # Stretches=myfit.Stretches, 
      # Stretch_sessions_per_week=myfit.Stretch_sessions_per_week, 
      
      # My_Fitness_activity_1=myfit.My_Fitness_activity_1, 
      # My_Fitness_activity_1_per_week=myfit.My_Fitness_activity_1_per_week, 
      
      # My_Fitness_activity_2=myfit.My_Fitness_activity_2, 
      # My_Fitness_activity_2_per_week=myfit.My_Fitness_activity_2_per_week)
      )
      
      print('valid')
      New_fit.save()

    else:
      print(form.errors)  

    if form.is_valid():
      print('main form valid') 
      obj=form.save(commit=False)
      obj=form.cleaned_data
      print('valid 2')
      
      myfit.Walking=obj['Walking']
      myfit.Walks_per_week=obj['Walks_per_week']
      myfit.Include_Walks=obj['Include_Walks']
      
      myfit.Jogging=obj['Jogging']
      myfit.Jogs_per_week=obj['Jogs_per_week']
      myfit.Include_Jogging=obj['Include_Jogging']
      
      myfit.Elliptic_Machine=obj['Elliptic_Machine']
      myfit.Elliptic_Machine_workouts_per_week=obj['Elliptic_Machine_workouts_per_week']
      myfit.Include_Elliptic=obj['Include_Elliptic']
      
      myfit.Weight_lifting=obj['Weight_lifting']
      myfit.Weight_lifting_per_week=obj['Weight_lifting_per_week']
      myfit.Include_Weights=obj['Include_Weights']
      
      myfit.Biking=obj['Biking']
      myfit.Bike_rides_per_week=obj['Bike_rides_per_week']
      myfit.Include_Biking=obj['Include_Biking']
      
      myfit.Zumba=obj['Zumba']
      myfit.Zumba_workouts_per_week=obj['Zumba_workouts_per_week']
      myfit.Include_Zumba=obj['Include_Zumba']
      
      myfit.Swimming=obj['Swimming']
      myfit.Swimming_sessions_per_week=obj['Swimming_sessions_per_week']
      myfit.Include_Swimming=obj['Include_Swimming']
      
      myfit.Martial_arts=obj['Martial_arts']
      myfit.Martial_arts_practices_per_week=obj['Martial_arts_practices_per_week']
      myfit.Include_Martialarts=obj['Include_Martialarts']
      
      # myfit.Bootcamp=obj['Bootcamp']
      # myfit.Bootcamp_workouts_per_week=obj['Bootcamp_workouts_per_week']
      # myfit.Include_Jogging=obj['Include_Jogging']
      
      # myfit.Taichi=obj['Taichi']
      # myfit.Taichi_practices_per_week=obj['Taichi_practices_per_week']
      # myfit.Include_Jogging=obj['Include_Jogging']
      
      # myfit.Sports=obj['Sports']
      # myfit.Sports_practices_per_week=obj['Sports_practices_per_week']
      
      # myfit.Pilates=obj['Pilates']
      # myfit.Pilates_practices_per_week=obj['Pilates_practices_per_week']
      
      myfit.Yoga=obj['Yoga']
      myfit.Yoga_practices_per_week=obj['Yoga_practices_per_week']
      myfit.Include_Yoga=obj['Include_Yoga']
      
      # myfit.Stretches=obj['Stretches']
      # myfit.Stretch_sessions_per_week=obj['Stretch_sessions_per_week']
      
      
      # myfit.My_Fitness_activity_1=obj['My_Fitness_activity_1']
      # myfit.My_Fitness_activity_1_per_week=obj['My_Fitness_activity_1_per_week']
      
 
      # myfit.My_Fitness_activity_2=obj['My_Fitness_activity_2']
      # myfit.My_Fitness_activity_2_per_week=obj['My_Fitness_activity_2_per_week']
      
      
      print('form passed')
      myfit.save()


      return redirect('landing')
     

    context={
          'form':form,
          # 'myfitness_ver':Myfitness_ver,
          'myfit':myfit,
        }
    print(context)
    return render(request, 'myfitness-update.html', context=context)       

# def MinorsymUpdateView(request):
#     current_user = CustomUser.objects.get(id=request.user.id)
#     form = MinorsymForm(request.POST or None, instance=current_user)
#     minorsym = Minorsym.objects.all().get(pk=request.user.id)
#     if form.is_valid():
#       obj=form.save(commit=False)
#       obj=form.cleaned_data

#       minorsym.Fatigue=obj['Fatigue']
#       minorsym.Lack_of_focus=obj['Lack_of_focus']
#       minorsym.Insomnia=obj['Insomnia']
#       minorsym.Migraine=obj['Migraine']
#       minorsym.Body_Pain=obj['Body_Pain']
#       minorsym.Minor_skin_issues=obj['Minor_skin_issues']
#       minorsym.Constipation=obj['Constipation']
#       minorsym.Frequent_sickness=obj['Frequent_sickness']
#       minorsym.ADD_ADHD=obj['ADD_ADHD']
#       minorsym.Low_motivation=obj['Low_motivation']
      
#       minorsym.save()
    
#       minorsym = Minorsym.objects.all().get(customuser=request.user.id)
#     form = MinorsymForm(request.POST or None)
#     context={
#           'form':form,
#           'minorsym':minorsym,
#         }

#     return render(request, 'minorsymUpdate.html', context=context)     

# def MajorsymUpdateView(request):
#     current_user = CustomUser.objects.get(id=request.user.id)
#     form = MajorsymForm(request.POST or None, instance=current_user)
#     majorsym = Majorsym.objects.all().get(pk=request.user.id)
#     if form.is_valid():
#       obj=form.save(commit=False)
#       obj=form.cleaned_data

#       majorsym.Cardiovascular_CVD=obj['Cardiovascular_CVD']
#       majorsym.Obesity=obj['Obesity']
#       majorsym.Pre_Diabetes=obj['Pre_Diabetes']
#       majorsym.Diabetes=obj['Diabetes']
#       majorsym.Hypothyroid=obj['Hypothyroid']
#       majorsym.Hyperthyroid=obj['Hyperthyroid']
#       majorsym.Arthritis=obj['Arthritis']
#       majorsym.Arthritis=obj['BP']
#       majorsym.Cancer=obj['Cancer']
#       majorsym.Osteoporosis=obj['Osteoporosis']
#       majorsym.Fibromylgia=obj['Fibromylgia']
#       majorsym.Alzheimers=obj['Alzheimers']
      
#       majorsym.save()
    
#       majorsym = Majorsym.objects.all().get(customuser=request.user.id)
#     form = MajorsymForm(request.POST or None)
#     context={
#           'form':form,
#           'majorsym':majorsym,
#         }

#     return render(request, 'majorsymUpdate.html', context=context)   

    

# def MyfastfoodsUpdateView(request):
#     current_user = CustomUser.objects.get(id=request.user.id)
#     form = MyfastfoodsForm(request.POST or None, instance=current_user)
   
#     myfastfoods = Myfastfoods.objects.all().get(pk=request.user.id)
#     print ( Myfastfoods.objects.all)
    
#     # print(myfastfoods.all)
#     if form.is_valid():
#       print('Valid')
#       obj=form.save(commit=False)
#       obj=form.cleaned_data

#       myfastfoods.Bacon=obj['Bacon']
#       myfastfoods.Burgers=obj['Burgers']
#       myfastfoods.Cookies=obj['Cookies']
#       myfastfoods.Frozen_pizza=obj['Cereals']
#       myfastfoods.Ice_cream=obj['Ice_cream']
#       myfastfoods.Pancakes=obj['Pancakes']
#       myfastfoods.Fried_foods=obj['Fried_foods']
#       myfastfoods.Fried_foods=obj['Frozen_pizza']
#       myfastfoods.Popcorn=obj['Popcorn']
#       myfastfoods.Frozen_meals=obj['Frozen_meals']
#       myfastfoods.French_fries=obj['French_fries']
#       myfastfoods.Potato_chips=obj['Potato_chips']
#       myfastfoods.Soft_drinks=obj['Soft_drinks']
#       myfastfoods.Milk_shakes=obj['Milk_shakes']
      
#       myfastfoods.save()
      
#       return redirect('landing')
#     #   myfastfoods = myfastfoods.objects.all().get(customuser=request.user.id)
#     # form = MajorSymptomsForm(request.POST or None)

#     else:
    
#       print(form.errors) 
#     context={
#           'form':form,
#           'myfastfoods':myfastfoods,
#         }

#     return render(request, 'myfastfoodsupdate.html', context=context) 


# dietician_group = create_dietician_group()

# dietician_group.permissions.remove(['can_add'])

# from rest_framework import viewsets
# class GoalsAPIView(viewsets.ModelViewSet):
#   queryset = Goals.objects.all()
#   serializer_class = GoalsSerializer

# class ProfileAPIView(viewsets.ModelViewSet):
#   queryset = MyProfile.objects.all()
#   serializer_class = ProfileSerializer

# working_directory = os.getcwd()
# print(working_directory)

# from django.http import HttpResponse
# from django.db import connection  # Import for database access
# import csv


# def sql(request):
#     cursor = connection.cursor()  # Use Django's cursor
#     cwd = os.getcwd()
#     print(cwd)
#     working_directory = os.getcwd()
#     print(working_directory)
#     try:
#         # Execute your query (replace with actual query)
#         cursor.execute("SELECT * FROM top3health_mytypmeals1")
#         records = cursor.fetchall()

#         if not records:
#             return HttpResponse('No data found.')

#         # Create CSV response
#         response = HttpResponse(content_type='text/csv')
#         response['Content-Disposition'] = 'attachment; filename=top3health_data.csv'

#         writer = csv.writer(response)
#         writer.writerow([column[0] for column in cursor.description])  # Header row
#         writer.writerows(records)

#         return response

#     except Error as e:
#         # Handle database errors
#         return HttpResponse(f'Error connecting to database: {str(e)}')

#     finally:
#         cursor.close()  # Close cursor  

# def sql1(request):
#  import mysql.connector, csv
#  from mysql.connector import Error

#  try:
#      connection = mysql.connector.connect(host='localhost',
#                                          database='top3db',
#                                          user='girish',
#                                          password='Mazatlan909.')
#      if connection.is_connected():
#         db_Info = connection.get_server_info()
#         print("Connected to MySQL Server version ", db_Info)
#         cursor = connection.cursor()
#         cursor.execute("select database();")
#         record = cursor.fetchall()
#         print("You're connected to database: ", record)
#         if records:
#             # Write data to CSV file
#             with open('mysql_file.csv', 'w', newline='') as csvfile:
#                 fieldnames = [column[0] for column in cursor.description]
#                 writer = csv.writer(csvfile)
#                 writer.writerow(fieldnames)
#                 writer.writerows(records)
#             logging.info("Data saved to mysql_file.csv")
#         else:
#             logging.warning("No data found in the table.")

        
#      for tables_name in cursor:
#          print(tables_name)
#          sql_select_Query = "select * from top3health_mytypmeals1 INTO OUTFILE './mysql_file.csv';"
#          cursor.execute(sql_select_Query)
#          records = cursor.fetchall()
#          print(records)

#  except Error as e:
#       print("Error while connecting to MySQL", e)
#  finally:
#       if connection.is_connected():
#         cursor.close()
#         connection.close()
#         print("MySQL connection is closed")

from django.http import HttpResponse
from django.db import connection  # Import for database access
import csv


def sql(request):
    cursor = connection.cursor()  # Use Django's cursor

    try:
        # Execute your query (replace with actual query)
        cursor.execute("SELECT * FROM top3health_mytypmeals1")
        records = cursor.fetchall()

        if not records:
            return HttpResponse('No data found.')

        # Create CSV response
        response = HttpResponse(content_type='text/csv')
        # response['Content-Disposition'] = 'attachment; filename=top3health_data.csv'
        response['Content-Disposition'] = 'attachment; filename=top3health_data.csv; path=/home/girish/Desktop/Django_projects/futurevision'
        writer = csv.writer(response)
        writer.writerow([column[0] for column in cursor.description])  # Header row
        writer.writerows(records)

        return response

    except Error as e:
        # Handle database errors
        return HttpResponse(f'Error connecting to database: {str(e)}')

    finally:
        cursor.close()  # Close cursor


def DV_data(request):

    import mysql.connector

    user = request.user

    myallergies = Myallergicfoods.objects.filter(customuser=user).order_by('-created_at').first()


    allergy1 = myallergies.allergicFood1
   

    context = {
      # myallergies: Myallergicfoods,
       'allergy1': myallergies.allergicFood1,
  
    }

    return render(request, 'plot_dv.html', context)

# def Profile_Detail_view(request,*args,custom_user_id):
#     queryset = MyProfile.objects.filter(id=custom_user_id)
    
#     serializer_class = ProfileSerializer
    
#     return JsonResponse(serializers.serialize('json', queryset), safe=False)
# def Goals_Detail_view(request,*args,custom_user_id):
#     queryset = Goals.objects.filter(id=custom_user_id)
    
#     serializer_class = GoalsSerializer
    
#     return JsonResponse(serializers.serialize('json', queryset), safe=False)

# class GoalsSerializerView():
#   serializer_class = GoalsSerializer()
#   def get(request,custom_user_id,*args,**kwargs):
#     queryset = Goals.objects.filter(id=custom_user_id)
#     serializer= serializer_class(queryset)
#     return {serializer.data, status=200}


# class DailylogView(TemplateView):
#  template_name = 'food_log2.html'    

# import logging

# def my_view(request):
#     logger = logging.getLogger(__name__)
#     study = Study.objects.filter(customuser=request.user).last()

#     print(mode)

#     logger.debug(f'Study object: {Study}')
#     logger.debug(f'mode: {mode}')

#     context = {
#         'study': Study,
#     }

#     return render(request, 'food_log2.html', context)       


# from django.shortcuts import redirect
# from django.contrib.auth.decorators import login_required
# from django.utils import timezone

# # Assuming your models are defined elsewhere


# def MyfoodgroupsView(request):
#     context = {}

#     if request.method == 'GET':
#         if request.user.is_authenticated:
#             custom_user = CustomUser.objects.get(pk=request.user.pk)
#             context['user'] = custom_user

#             # Check if the modal was closed and handle accordingly
#             if 'modal_closed' in request.session:
#                 del request.session['modal_closed']
#                 # Redirect to a specific page or perform other actions
#                 return redirect('myfitness')  # Example: Redirect to myfitness page

#             # ... (rest of your logic to render the "myfoods" page)
#             return render(request, 'myfoodgroups.html', context=context)
#         else:
#             return redirect('login')

#     elif request.method == 'POST':
#         if 'modal_closed' in request.POST:
#             request.session['modal_closed'] = True
#             return redirect('myfoodgroups')
#         else:
#             form = MyfoodgroupsForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 # Redirect to the desired page after saving
#                 return redirect('myfitness')
#             else:
#                 context['form'] = form
#                 return render(request, 'myfoodgroups.html', context=context)

# def MyfoodgroupsView(request):
#     form = MyfoodgroupsForm(request.POST or None)
    
#     if form.is_valid():
#       if 'modal_closed' in request.POST:
#         obj = form.save(commit=False)
#         obj.customuser_id=(request.user.id)
#         obj.save()
#     return redirect('myfitness') 
#     context={'form':form}
 
#     template_name = 'myfoodgroups.html'
#     return render(request, 'myfoodgroups.html', context=context)


#NEWEST

# def MyfoodgroupsView(request):
#         form = MyfoodgroupsForm(request.POST or None)
#         if form.is_valid():
            
#                 obj = form.save(commit=False)
#                 obj.customuser_id = (request.user.id)
#                 obj.save()
#                 return redirect('/myfitness') 
   
#         context={'form':form}
#         template_name = 'myfoodgroups.html'
#         return render(self.request, 'myfoodgroups.html', context=context)  

def MyfoodgroupsView(request):
    if request.user.is_authenticated:
        form = MyfoodgroupsForm(request.POST or None)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.customuser = request.user  # Assign user object directly
            obj.save()
            return redirect('/myfitness') 
        context={'form':form}
        template_name = 'myfoodgroups.html'
        return render(request, 'myfoodgroups.html', context=context)
    else:
        return redirect('login')

    # context = {}
    # user = request.user.id
    # if request.method == 'GET':
    #     if request.user.is_authenticated:
    #         custom_user = CustomUser.objects.get(pk=request.user.pk)
    #         context['user'] = custom_user
    #         # ... (rest of your logic for rendering the "myfoods" page)
    #         return render(request, 'myfoodgroups.html', context=context)
    #     else:
    #         # Handle unauthenticated users (e.g., redirect to login)
    #         return redirect('login')

    # if request.method == 'POST':
    #     if 'modal_closed' in request.POST:
    #         # Handle the case where the modal was closed
    #         request.session['modal_closed'] = True
    #         return redirect('myfoodgroups')
    #     else:
    #         form = MyfoodgroupsForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             return redirect('myfitness')  # Redirect to myfitness page
    #         else:
    #             context['form'] = form
    #             return render(request, 'myfoodgroups.html', context=context)
# def MyfoodgroupsView(request):
#     context = {}

#     if request.method == 'GET':
#         if request.user.is_authenticated:
#             custom_user = CustomUser.objects.get(pk=request.user.pk)
#             print(custom_user)
#             context['user'] = custom_user
#             # Check if the modal was closed and reset the flag
#             if 'modal_closed' in request.session:
#                 del request.session['modal_closed']
#         # ... (rest of your logic to render the "myfoods" page)
#         return render(request, 'myfoodgroups.html', context=context)

#     elif request.method == 'POST':
#         if 'modal_closed' in request.POST:
#             # Handle the case where the modal was closed
#             request.session['modal_closed'] = True  # Set the flag
#             return redirect('myfoodgroups')
#         else:
#             # Handle form submission and save data
#             # ... (your form handling logic)
#             return redirect('myfoodgroups')        

# def MyfoodgroupsView(request):
#   context = {}
#   if request.method == 'GET':
#     if request.user.is_authenticated:
#       custom_user = CustomUser.objects.get(pk=request.user.pk)
#       print(custom_user)
#       context['user'] = custom_user 
#     # Logic to render the "myfoods" page (explained below)
#     return render(request, 'myfoodgroups.html', context=context)
#   elif request.method == 'POST':
#     if 'modal_closed' in request.POST:
#       # Handle the case where the modal was closed
#       return redirect('myfoodgroups')
#     else:
#       return render(request, 'flashpage.html')    

# def MyfoodgroupsView(request):
#   context = {}
#   if request.method == 'GET':
#     if request.user.is_authenticated:
#       custom_user = CustomUser.objects.get(pk=user.pk)
#       print(custom_user)
#       context['user'] = custom_user 
#       print(context)
#     # Logic to render the "myfoods" page (explained below)
#     return render(request, 'myfoodgroups.html', context=context)  # Add necessary context data
#   elif request.method == 'POST':
#     if 'modal_closed' in request.POST:
#       # Handle the case where the modal was closed
#       return redirect('myfitness')
#     else:
#       return render(request, 'myfoodgroups.html')   

# def flashpageView(request):
#   if request.user.is_authenticated:
#     user = request.user
#   if user:
#     print(user)
#     if 'user' and 'modal_closed' in request.session:
#       # del request.session['modal_closed']
#       return redirect('/myfoodgroups')
#     # Your logic for the flash page
#     return render(request, 'flashpage.html')
#   else:
#     return redirect('login')     

# def flashpageView(request):
#   # if request.user.is_authenticated:
#   #   print(request.user)
#   #   print(request.user.is_active)
#   #   print(request.user.is_staff)
#     # Your logic for the flash page
#     return render(request, 'flashpage.html')
  # else:
  #   return redirect('login')  # 

# def MyfoodgroupsView(request):
  
#   if request.user.is_authenticated:
#         print(request.user)
#   if request.method == 'GET':
#     print("get")
    
#     if request.user.is_authenticated:
#       print('auth')
#       custom_user = CustomUser.objects.get(pk=request.user.id)
#       print(custom_user)
#       context['user'] = custom_user
#       print(request.user.id)
#     else:
#       return redirect('login')  
#     return render(request, 'myfoodgroups.html', context=context)

#   elif request.method == 'POST':
    
#     form = MyfoodgroupsForm(request.POST)
#     if form.is_valid():
     
#       form.save()
#       return redirect('myfitness')  
#     else:
#       context['form'] = form
#       return render(request, 'myfoodgroups.html', context=context)