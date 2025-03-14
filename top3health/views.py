# Create your views here.
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, ListView
from .forms import CustomUserCreationForm,   MyfitnessForm, MyfoodgroupsForm
from .forms import BeginpageForm 
from .forms import MyfoodsuggestionsForm
from .forms import HealthsymForm
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views import generic
from django.contrib.auth.decorators import login_required
from .forms import StudyForm
from .forms import MydailylogForm
from .models import Myhealthscreening
from .models import Myfitness
from .models import Dietician_note
from .models import Healthsym
from .models import Myfoodsuggestions
from .models import Study
from .models import Myexpenses
from .models import Myhabits
from .models import CustomUser
from .models import Supplements
from .models import Myfoodgroups
from .models import Myallergicfoods
from .models import Mytypmeals1
from .models import Beginpage
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render
from rest_framework import generics
from django.core import serializers
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
from .forms import Mytypmeals1Form
from .forms import SupplementsForm
from .forms import  DieticiannoteForm
from django.db.models import Q
from django.contrib.auth import logout

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
from mysql.connector import Error
import mysql.connector
import io


# from django.contrib.auth.views import login

import datetime

from django.conf import settings

print(settings.SESSION_COOKIE_AGE)

class flashpageView(TemplateView):
 template_name = 'flashpage.html'


class MyLoginView(LoginView):
    template_name = 'registration/login.html'

    def form_valid(self, form):
        user = form.get_user()
        print(user)

        if user.is_superuser:
            return redirect('admin:index') 

        if user.is_staff and user.groups.filter(name='dietician').exists():
            return redirect('dietician_dashboard')    

        response = super().form_valid(form)

        if user.last_login is None:
            return redirect('flashpage') 

        try:
           healthsym_records = Healthsym.objects.filter(customuser=user)
           if healthsym_records.exists():
            healthsym_record = healthsym_records.first()
           else:
            return redirect('minorsym')
        except Healthsym.DoesNotExist:
             return redirect('minorsym') 

        try:
            Myfitness.objects.get(customuser=user) #add filter
        except Myfitness.DoesNotExist:
            return redirect('Myfitness')

        try:
            Myfoodgroups.objects.get(customuser=user) #add filter
        except Myfoodgroups.DoesNotExist:
            return redirect('Myfoodgroups')

        try:
            Myfoodsuggestions.objects.get(customuser=user) #add filter
        except Myfoodsuggestions.DoesNotExist:
            return redirect('mybreakfastdesign')

        try:
            Supplements.objects.get(customuser=user) #add filter
        except Supplements.DoesNotExist:
            return redirect('Supplements')   

        # try:
        #     Myhabits.objects.get(customuser=user) #add filter
        # except Myexpenses.DoesNotExist: #correct error here.
        #     return redirect('Myhabits')  

        try:
           myhabits_records = Healthsym.objects.filter(customuser=user)
           if myhabits_records.exists():
            myhabits_record = healthsym_records.first()
           else:
            return redirect('myhabits')
        except Healthsym.DoesNotExist:
             return redirect('myhabits') 

        try:
            Myexpenses.objects.get(customuser=user) #add filter
        except Myexpenses.DoesNotExist: #correct error here.
            return redirect('Myexpenses')      

        return redirect('landing')


# class MyLoginView(LoginView):
#     template_name = 'registration/login.html'

#     def form_valid(self, form):
#         user = form.get_user()
#         print(user)

#         if user.is_superuser:
#             return redirect('admin:index') 

#         if user.is_staff and user.groups.filter(name='dietician').exists():
#             return redirect('dietician_dashboard')    

#         if user.last_login is None:
#             return redirect('flashpage') 

#         #Check if data exists in MyFoodGroups table for the current user
#         try:
#             minorsym.objects.get() 
#         except minorsym.DoesNotExist:
#             return redirect('Minorsym') 
#         try:
#             Myfitness.objects.get() 
#         except Myfitness.DoesNotExist:
#             return redirect('Myfitness')
#         try:
#             Myfoodgroups.objects.get() 
#         except Myfoodgroups.DoesNotExist:
#             return redirect('Myfoodgroups')
#         try:
#             Mybreakfastdesign.objects.get() 
#         except Mybreakfastdesign.DoesNotExist:
#             return redirect('Mybreakfastdesign')
#         try:
#             Supplements.objects.get() 
#         except Supplements.DoesNotExist:
#             return redirect('Supplements')    
#         try:
#             Myexpenses.objects.get() 
#         except Myexpensess.DoesNotExist:
#             return redirect('Myexpenses')    

#         return redirect('landing')

@login_required
def MyfoodgroupsView(request):
        if request.user.is_authenticated:
         User = get_user_model()
         print("now printing request.user")
         print(request.user)
         current_user = User.objects.get(pk=request.user.pk)
         print("now printing current_user")
         print(current_user)
         print(f"Session in MyfoodgroupsView: {request.session.items()}")
        form = MyfoodgroupsForm(request.POST or None)
        
        if form.is_valid():
            obj = form.save(commit=False)
            print(request.user.id)
            obj.customuser = request.user
            print(obj.customuser)  # Assign user object directly
            obj.save()
            return redirect('/mybreakfastdesign') 
        else:    
            print(form.errors)
        context={'form':form,
                  'myfoodgroups':Myfoodgroups,
                  'user':request.user}
        template_name = 'myfoodgroups.html'
        return render(request, 'myfoodgroups.html', context=context)              
 
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
  return render(request, 'registration/signup.html', context=context)
  template_name = 'registration/signup.html'
  return render(request, 'registration/signup.html', {'alert_flag': True})


class HomePageView(TemplateView):
 template_name = 'top3health-bootstrap.html'



# def staff_register(request):
#     if request.method == 'POST':
#         form = StaffRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             # Don't call login(request, user) here
#             return redirect('login')  # Redirect to login page after successful registration
#     else:
#         form = StaffRegistrationForm()  # Pre-populate if needed
#     return render(request, 'staff_registration.html', {'form': form})
     
        
class LandingView(TemplateView):
  success_url = reverse_lazy('landing')
  template_name = 'landing-bootstrap.html'
  # context={"user":User}
  #pass goals into context


# def DailylogView(request):
#     if request.user.is_authenticated:
#         try:
#             myfitness_record = request.user.myfitness 
#             moderate_intensity = myfitness_record.moderate_intensity 
#             print(f"moderate_intensity: {moderate_intensity}") 
#         except Myfitness.DoesNotExist:
#             moderate_intensity = None 
#             print("Myfitness record does not exist.")

#         form = MydailylogForm(request.POST or None)
#         if form.is_valid():
#             obj = form.save(commit=False)
#             obj.customuser_id = request.user.id 
#             obj.save()
#             return redirect('landing')

#         context = {
#             'form': form,
#             'myfitness': myfitness_record 
#         }
#         return render(request, 'food_log2.html', context)

#     else:
#         return redirect('login') 

# def DailylogView(request):
#     if request.user.is_authenticated:
#         try:
#             myhabits_record = request.user.myhabits 
#             Stretches = myhabits_record.Stretches 
#             print(f"Stretches: {Stretches}") 
#         except Myhabits.DoesNotExist:
#             Stretches = None 
#             print("Myhabits record does not exist.")

#         form = MydailylogForm(request.POST or None)
#         if form.is_valid():
#             obj = form.save(commit=False)
#             obj.customuser = request.user
#             obj.save()
#             return redirect('landing')

#         context = {
#             'form': form,
#             'myhabits': myhabits 
#         }
#         return render(request, 'food_log2.html', context)

#     else:
#         return redirect('login') 
        
@login_required
def DailylogView(request):
    if request.user.is_authenticated:
        myhabits_record = request.user.myhabits.last() 
        # print(myhabits_record.__dict__)
        
        if myhabits_record:
            Stretches = myhabits_record.Stretches
            print(Stretches)
            Reduce_processed = myhabits_record.Reduce_processed
            # print(Reduce_processed)
            Prepare_meals = myhabits_record.Prepare_meals
            # print(Prepare_meals)
            Wake_time = myhabits_record.food_cost_savings
            food_cost_savings = myhabits_record.Clear_kitchen
            Clear_kitchen = myhabits_record.Stretches
            Brush_Floss = myhabits_record.Brush_Floss
            Groceries_shop = myhabits_record.Groceries_shop
            daily_mindfulness = myhabits_record.daily_mindfulness
            food_suggestions = myhabits_record.food_suggestions
            reduce_alcohol = myhabits_record.reduce_alcohol
            reduce_smoking = myhabits_record.reduce_smoking
            custom_habit_1 = myhabits_record.custom_habit_1
            custom_habit_2 = myhabits_record.custom_habit_2
            custom_habit_3 = myhabits_record.custom_habit_3 
        else:
            Stretches = None

            print("Myhabits record does not exist.")
            

        form = MydailylogForm(request.POST or None)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.customuser = request.user
            obj.save()
            return redirect('landing')
        else: 
            print(form.errors)
        context = {
            'form': form,
            'myhabits': myhabits_record #pass the myhabits_record
        }
        return render(request, 'food_log2.html', context)        

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

def dietician_dashboard(request):
    # ... your logic for the dietician dashboard ...
    return render(request, 'dietician_dashboard.html') 


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


def MyHealthscreeningView(request):
  form=MyhealthscreeningForm(request.POST or None)
  if form.is_valid():
    print(request.user.id)
    obj = form.save(commit=False)
    obj.customuser_id=(request.user.id)
    obj.save()
    return redirect('/landing')
  print(form.errors)
  # form= ProfileForm()
  context={'form':form}
  template_name = 'healthscreening.html'
  return render(request, 'healthscreening.html', context=context)

@login_required
def MinorsymView(request):
  form=HealthsymForm(request.POST or None)
  if form.is_valid():
    
    obj = form.save(commit=False)
    # obj.customuser_id=(request.user.id)
    obj.customuser = request.user
    print(obj)
    obj.save()
    return redirect('myfitness')
  print(form.errors)
 
  context={'form':form}
  template_name = 'minorsymptoms-bootstrap.html'
  return render(request, 'minorsymptoms-bootstrap.html', context=context)


@login_required
def MinorsymUpdateView(request):
    current_user = request.user
    minorsym = None  # Initialize minorsym

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
        minorsym = Healthsym.objects.filter(customuser=current_user).order_by('-created_at').first()
        form = HealthsymForm(instance=minorsym) #correct instance variable

    context = {
        'form': form,
        'minorsym': minorsym,
    }
    return render(request, 'minorsymupdate.html', context)


def MyhabitsView(request):
  form=MyhabitsForm(request.POST or None)  
  if form.is_valid():
    print('Valid')
    obj = form.save(commit=False)
    obj.customuser_id=(request.user.id)
    obj.save()
    return redirect('/myexpenses') 
  else:
     print(form.errors)   
  context={'form':form}
  template_name = 'myhabits.html'
  return render(request, 'myhabits.html', context=context)
  print(request.user)    


@login_required
def MyhabitsupdateView(request):
    current_user = request.user
    myhabits = None  # Initialize minorsym

    if request.method == 'POST':
        form = MyhabitsForm(request.POST)
        if form.is_valid():
            myhabits = form.save(commit=False)
            myhabits.customuser = current_user
            myhabits.created_at = timezone.now()
            myhabits.save()
            return redirect('/landing')
    else:
        print("error in myhabits form?")
        myhabits = Myhabits.objects.filter(customuser=current_user).order_by('-created_at').first()
        form = MyhabitsForm(instance=myhabits) #correct instance variable

    context = {
        'form': form,
        'myhabits': myhabits,
    }
    return render(request, 'myhabitsupdate.html', context)  


def MyfitnessView(request):
  form=MyfitnessForm(request.POST or None)  
  if form.is_valid():
    obj = form.save(commit=False)
    obj.customuser_id=(request.user.id)
    obj.save()
    return redirect('myfoodgroups') 
  context={'form':form}
  # print("form : "+str(form))
  template_name = 'myfitness-bootstrap.html'
  return render(request, 'myfitness-bootstrap.html', context=context)
  # return render(request, 'myfitness-bootstrap.html', {'alert_flag': True})
  print(request.user)

def MysettingsView(request):
   return render(request, 'settings.html')

def MyprofileandgoalsView(request):   
   return render(request, 'myprofileandgoals.html')

def MybreakfastdesignView(request):
  form=MyfoodsuggestionsForm(request.POST or None)  
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

def MysupplementsView(request):
  form=SupplementsForm(request.POST or None)  
  if form.is_valid():
    print("Valid")
    print(request.user) 
    obj = form.save(commit=False)
    obj.customuser_id=(request.user.id)
    obj.save()
    return redirect('myhabits')
  else:
   
    print(form.errors)   
 
  context={'form':form}
  return render(request, 'supplements.html', context=context)
  template_name = 'supplements.html'
  # return render(request, 'supplements.html', {'alert_flag': True})
  print(request.user) 

import numpy as np
import seaborn as sns

from django.http import HttpResponse
from django.db import connection  # Import for database access
import csv

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


# from django.contrib.auth import get_user_model
# from django.views.decorators.cache import never_cache
# @never_cache

@login_required
def list_users(request):

    dietician_username = request.session.get('dietician_username') # Retrieve from the session
    print(f"Dietician username from session: {dietician_username}")
    print(type(request.user))  # Print the type of request.user

    User = get_user_model()
    if isinstance(request.user, User):  # Check if it's your custom user model
        current_user = request.user
    else:
        current_user = User.objects.get(pk=request.user.pk) # Get the CustomUser instance

    current_user = CustomUser.objects.get(id=request.user.id) 
    
    if request.user.is_authenticated:
         
         print("now printing request.user")
         print(request.user)
    
    users = CustomUser.objects.exclude(Q(username='juhik') | Q(is_superuser=True))
    allowed_user = CustomUser.objects.get(username='juhik')
    print(allowed_user)

    user_data = []
    for user in users:
        latest_healthsym = user.healthsym_set.order_by('-created_at').first()

        # Initialize variables *outside* the try block
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
        veggies = None
        beans_lentils = None
        fruits_berries = None
        protein = None
        dairy = None
        grains = None

        moderate_intensity = None
        vigorous_intensity = None
        muscle_build = None
        balance = None

        try:
            myfoodgroups_record = user.myfoodgroups  # Access directly
            veggies = myfoodgroups_record.All_veggies if myfoodgroups_record else None
            beans_lentils = myfoodgroups_record.Beans_Lentils if myfoodgroups_record else None
            fruits_berries = myfoodgroups_record.Fruits_Berries if myfoodgroups_record else None
            protein = myfoodgroups_record.Protein if myfoodgroups_record else None
            dairy = myfoodgroups_record.Dairy if myfoodgroups_record else None
            grains = myfoodgroups_record.Grains if myfoodgroups_record else None

        except Myfoodgroups.DoesNotExist:
            pass # All the values are already initialized to None

        try:
             myfitness_record = user.myfitness
             moderate_intensity = myfitness_record.moderate_intensity if myfitness_record else None
             vigorous_intensity = myfitness_record.vigorous_intensity if myfitness_record else None
             muscle_build = myfitness_record.muscle_build if myfitness_record else None
             balance = myfitness_record.balance if myfitness_record else None

        except Myfitness.DoesNotExist:
            pass # All the values are already initialized to None
                 
        
        if latest_healthsym: # Check if it exists before accessing attributes
            minor1 = latest_healthsym.Minor1
            print(minor1)
            minor2 = latest_healthsym.Minor2
            minor3 = latest_healthsym.Minor3
            minor4 = latest_healthsym.Minor4
            minor5 = latest_healthsym.Minor5
            major1 = latest_healthsym.Major1
            major2 = latest_healthsym.Major2
            major3 = latest_healthsym.Major3
            major4 = latest_healthsym.Major4
            major5 = latest_healthsym.Major5

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
            'veggies': veggies,
            'beans_lentils': beans_lentils,
            'fruits_berries': fruits_berries,
            'dairy': dairy,
            'grains': grains,
            'moderate_intensity': moderate_intensity,
            'vigorous_intensity': vigorous_intensity,
            'muscle_build': muscle_build,
            'balance': balance,
        })

    form = DieticiannoteForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        # ... any other processing for the form ...

    context = {
        'users': user_data,
        'form': form,  # Include the form in the context
        'allowed_user': allowed_user,
    }
    template_name = 'dietician_dashboard.html'

    return render(request, template_name, context=context)   

@login_required
def health_dashboard(request):
    try:
        myfoodgroups = request.user.myfoodgroups
        myfitness = request.user.myfitness
        myexpenses = request.user.myexpenses

        # Prepare food data
        food_data = {
            'Categories': ['Veggies', 'Beans', 'Fruits', 'Protein', 'Dairy', 'Grains'],
            'Your Intake': [myfoodgroups.All_veggies, myfoodgroups.Beans_Lentils, myfoodgroups.Fruits_Berries, 
                           myfoodgroups.Protein, myfoodgroups.Dairy, myfoodgroups.Grains],
            'USDA': [2.5, 1.5, 2.0, 5.0, 3.0, 3.0]
        }
        food_df = pd.DataFrame(food_data)
        food_df = food_df.melt(id_vars='Categories', var_name='Source', value_name='Intake')

        # Prepare fitness data
        fitness_data = {
            'Categories': ['Moderate', 'Vigorous', 'Muscle', 'Balance'],
            'Your Duration': [myfitness.moderate_intensity, myfitness.vigorous_intensity, 
                             myfitness.muscle_build, myfitness.balance],
            'HHS': [300, 75, 60, 100]
        }
        fitness_df = pd.DataFrame(fitness_data)
        fitness_df = fitness_df.melt(id_vars='Categories', var_name='Source', value_name='Duration')

        # Prepare weekly expense data
        weekly_expense_data = {
            'Category': ['Misc', 'Eat Out', 'Groceries',],
            'Cost': [
                 myexpenses.Misc_expenses,
                myexpenses.weekly_eatout_cost, 
                myexpenses.weekly_grocery_cost, 
                
            ]
        }
        weekly_expense_df = pd.DataFrame(weekly_expense_data)

        # Prepare monthly expense data
        monthly_expense_data = {
            'Category': ['Gym','OOP','Insurance', 'Office Visit', 'Prescriptions'],
            'Cost': [
                myexpenses.gym_cost, 
                myexpenses.oop_cost, 
                myexpenses.insurance_premium, 
                myexpenses.office_visit_cost, 
                myexpenses.prescription_cost, 
            ]
        }
        monthly_expense_df = pd.DataFrame(monthly_expense_data)

        # Create Seaborn plots
        sns.set_theme(style="white")  # Set style to 'white' to remove gridlines
        fig, axes = plt.subplots(2, 2, figsize=(10, 8), gridspec_kw={'hspace': 0.5, 'wspace': 0.05}) 
        plt.subplots_adjust(left=0.1, right=0.95, top=0.92, bottom=0.05)
        # Food Plot
        sns.barplot(x='Categories', y='Intake', hue='Source', data=food_df, palette=["#377eb8", "#e41a1c"], ax=axes[0, 0], width=0.6, edgecolor='white')
        axes[0, 0].set_ylabel('Cup Servings', fontsize=15)
        axes[0, 0].set_title('Food Intake vs. USDA', y=1.07, fontsize=15)
        axes[0, 0].tick_params(axis='x', labelsize=11)
        axes[0, 0].legend(fontsize=13)
        axes[0, 0].set_xlabel('')  # Remove x-axis label
        for spine in axes[0, 0].spines.values():
            spine.set_linewidth(0.5) 
            spine.set_color('white')

        # Fitness Plot
        sns.barplot(x='Categories', y='Duration', hue='Source', data=fitness_df, palette=["#1f77b4", "#9467bd"], ax=axes[1, 0], edgecolor='white')
        axes[1, 0].set_ylabel('Minutes', fontsize=15)
        axes[1, 0].set_title('Fitness Duration vs. HHS', y=1.07, fontsize=15)
        axes[1, 0].tick_params(axis='x', labelsize=12)
        axes[1, 0].legend(fontsize=13)
        axes[1, 0].set_xlabel('')  # Remove x-axis label
        for spine in axes[1, 0].spines.values():
            spine.set_linewidth(0.5)
            spine.set_color('white')


        # Weekly Expenses Pie Chart
        labels=weekly_expense_df['Category']
       
        axes[0, 1].pie(weekly_expense_df['Cost'], labels=weekly_expense_df['Category'], autopct=lambda p: f'${round(p/100*weekly_expense_df["Cost"].sum())}', 
        startangle=90, textprops={'fontsize': 12}, radius=1.0)
        axes[0, 1].set_title('Weekly Expenses', y=0.18)
        
        for spine in axes[1, 1].spines.values():
            spine.set_linewidth(0.5)

        # Monthly Expenses Pie Chart
        axes[1, 1].pie(monthly_expense_df['Cost'], labels=monthly_expense_df['Category'], autopct=lambda p: f'${round(p/100*monthly_expense_df["Cost"].sum())}', 
        startangle=90, textprops={'fontsize': 12},radius=1.0)
        axes[1, 1].set_title('Monthly Expenses', y=0.19)

        axes[0, 1].set_title('Weekly Expenses', fontsize=15 )  # Changed title text
        axes[1, 1].set_title('Monthly Expenses', fontsize=15) # Changed title text


        fitness_data_wide = fitness_df.pivot(index='Categories', columns='Source', values='Duration')

        food_data_wide = food_df.pivot(index='Categories', columns='Source', values='Intake')
        for category in food_data_wide.index:
          your_intake = food_data_wide.loc[category, 'Your Intake']
          usda_intake = food_data_wide.loc[category, 'USDA']

          if usda_intake != 0:  # Avoid division by zero
            percentage_of_usda = (your_intake / usda_intake) * 100  # Calculate as % of USDA
            axes[0, 0].annotate(f"{percentage_of_usda:.1f}%", 
                                xy=(category, max(your_intake, usda_intake) + 0.17),  # Adjust vertical offset as needed
                                ha='center', fontsize=12, color='black')  # Adjust color as needed
          else:
            axes[0, 0].annotate("N/A",  # Or some other indicator for zero USDA
                                xy=(category, max(your_intake, usda_intake) + 0.17),
                                ha='center', fontsize=12, color='black')

        for category in fitness_data_wide.index:
          your_duration = fitness_data_wide.loc[category, 'Your Duration']
          hhs_duration = fitness_data_wide.loc[category, 'HHS']

          if hhs_duration != 0:  # Avoid division by zero
            percentage_of_hhs = (your_duration / hhs_duration) * 100  # Calculate as % of HHS
            axes[1, 0].annotate(f"{percentage_of_hhs:.1f}%", 
                                xy=(category, max(your_duration, hhs_duration) + 0.27),  # Adjust offset as needed
                                ha='center', fontsize=12, color='black')  # Adjust color as needed
          else:
            axes[1, 0].annotate("N/A",  # Or some other indicator for zero HHS
                                xy=(category, max(your_duration, hhs_duration) + 0.27),
                                ha='center', fontsize=12, color='black')                         

        # 
        # plt.rcParams['figure.constrained_layout.use'] = True
        plt.savefig('fig.png',bbox_inches='tight')

        # Convert plot to image
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        plt.close()
        image_data = base64.b64encode(buf.getvalue()).decode('utf-8')

        return render(request, 'landing-bootstrap.html', {'image_data': image_data})

    except (Myfoodgroups.DoesNotExist, Myfitness.DoesNotExist, Myexpenses.DoesNotExist):
        return render(request, 'missing_data.html')      

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------    
def testauthview(request):
    if request.user.is_authenticated:
        print(request.user)
        print(request.user.username)
        username = request.user.username
    return HttpResponse(f"Hello, {username}!")
        # return HttpResponse("User is authenticated")
    # else:
    return HttpResponse("User is not authenticated")  

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

# def GoalsView(request):
#   form=GoalsForm(request.POST or None)
#   if form.is_valid():
#     obj = form.save(commit=False)
#     print(request.user.id)
#     # print(obj.user.id)
#     obj.customuser_id=(request.user.id)
#     obj.save()
    
#     # print (Customuser.Regular_or_Study_Mode)
#     return redirect('/myprofile')
     
#   print(form.errors)
#   context={'form':form}
#   template_name = 'goals-bootstrap.html'
#   return render(request, 'goals-bootstrap.html', context=context)

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

# class MyLoginView(LoginView):
#     def form_valid(self, form):
#         user = form.get_user()
#         print("inside myloginview")
#         print(user.last_login)
#         print(user.role)
#         print(user)
#         user = CustomUser.objects.get(pk=user.id)
#         print(user)
   

        # context={'form':form}
        # if (not user.last_login) and (user.role !='dietician'):
        #     print("First login!")
        # return redirect('landing')
        # else: return redirect('landing')
            
        # else:
        #     return super().form_valid(form)


# def health_dashboard(request):
#     try:
#         connection = mysql.connector.connect(
#             host='localhost',
#             database='top3db',
#             user='girish',
#             password='Mazatlan909.'
#         )

#         if connection.is_connected():
#             sql_query_df_food = pd.read_sql_query('SELECT * FROM top3health_myfoodgroups', con=connection)
#             df_food = pd.DataFrame(sql_query_df_food)
#             print(df_food)
#             sql_query_df_fit = pd.read_sql_query('SELECT * FROM top3health_myfitness', con=connection)
#             df_fit = pd.DataFrame(sql_query_df_fit)
#             print(df_fit)

#     except Error as e:
#         print("Error while connecting to MySQL", e)
#         return HttpResponse(status=500)

#     # Prepare the food data for plotting
#     colors1 = {'USDA': 'steelblue',
#               'Your food intakes': 'firebrick'}
#     food_data = df_food.values[0][1:7]  # Assuming first row (index 0) has data
#     food_categories = ['Veggies', 'Beans', 'Fruits', 'Protein', 'Dairy', 'Grains']
#     your_food_intake = food_data  # Assuming the first column is the user ID
#     usda_recommendations = [2.5, 1.5, 2.0, 5.0, 3.0, 3.0]
#     plot_height = 180


#     # Prepare the fitness data for plotting
#     fitness_categories = ['Moderate', 'Vigorous', 'Muscle', 'Balance']
#     fitness_data = df_fit.values[0][1:5]  # Assuming first row (index 0) has data
#     your_workout_duration = fitness_data
#     hhs_recommendations = [300, 75, 60, 100]

#     # Create two subplots for food and fitness data
#     fig, (ax_food, ax_fit) = plt.subplots(2, 1, figsize=(3.5, 4))

#     # Food Intake Chart
#     x = np.arange(len(food_categories))  # Create x-axis positions
#     width = 0.35  # Width of the bars
#     ax_food.bar(x - width/2, your_food_intake, width, color=colors1['Your food intakes'], label='Your Data')
#     ax_food.bar(x + width/2, usda_recommendations, width, color=colors1['USDA'], label='USDA')
#     ax_food.set_xticks(x)
#     ax_food.set_xticklabels(food_categories, rotation=0, ha='center')
#     #bars1 = ax_food.bar(food_categories, your_food_intake, color=colors1['Your food intakes'], label='Your food Data')
#     #bars2 = ax_food.bar(food_categories, usda_recommendations, bottom=your_food_intake, color=colors1['USDA'], label='USDA')
#     # ax_food.set_xlabel('Food Categories',  fontsize=8)
#     ax_food.set_ylabel('Cup Servings', fontsize=8)
#     ax_food.set_title('Food Intake vs. USDA', fontsize=10)
#     ax_food.legend(fontsize=7)
#     ax_food.tick_params(axis='x', labelsize=7)
   

#     colors2 = {'HHS': '#1f77b4',
#               'Your workout duration': '#ff7f0e'}

#     # Fitness Chart
#     x = np.arange(len(fitness_categories))  # Create x-axis positions
#     width = 0.3  # Width of the bars
#     ax_fit.bar(x - width/2, your_workout_duration, width, color=colors2['Your workout duration'], label='Your Duration', edgecolor="none", linewidth=0.15)
#     ax_fit.bar(x + width/2, hhs_recommendations, width, color=colors2['HHS'], label='HHS', edgecolor='none', linewidth=0.15)
#     ax_fit.set_xticks(x)
#     ax_fit.set_xticklabels(fitness_categories, rotation=0, ha='center')
#     # bars3 = ax_fit.bar(fitness_categories, your_workout_duration, color=colors2['Your workout duration'], label='Your fitness')
#     # bars4 = ax_fit.bar(fitness_categories, hhs_recommendations, bottom=your_workout_duration, color=colors2['HHS'], label='HHS')
#     # ax_fit.set_xlabel('Fitness Categories',  ha='center')
#     ax_fit.set_ylabel('Minutes', fontsize=8)
#     ax_fit.set_title('Fitness Duration vs. HHS', fontsize=10)
#     ax_fit.legend(fontsize=7)
    
#     plt.rcParams['font.family'] = 'sans-serif' 
#     #plt.rcParams['font.sans-serif'] = 'Arial'  # 
#     # Adjust layout to prevent overlapping plots
#     # ax_food.yaxis.tick_right()
#     # ax_food.yaxis.set_label_position("right")
#     # ax_food.yaxis.tick_left()
#     # ax_food.yaxis.set_label_position("left")
#     # ax_fit.yaxis.tick_right()
#     # ax_fit.yaxis.set_label_position("right")
#     plt.tight_layout()
#     plt.subplots_adjust(hspace=0.65)
#     plt.tick_params(axis='x', labelsize=7)

#     for spine in ax_food.spines.values():
#       spine.set_linewidth(0.2)  # Adjust linewidth as needed

#     for spine in ax_fit.spines.values():
#       spine.set_linewidth(0.2) 

#     # Combine both figures into a single image
#     buf = io.BytesIO()
#     plt.savefig(buf, format='png')
#     plt.close()
#     response = HttpResponse(buf.getvalue(), content_type='image/png')
#     image_as_string = base64.b64encode(buf.getvalue()).decode('utf-8')

#     # Return the rendered template with the image data
#     return render(request, 'landing-bootstrap.html', {'image_data': image_as_string})

# @login_required
# def health_dashboard(request):
#     try:
#         myfoodgroups = request.user.myfoodgroups
#         myfitness = request.user.myfitness

#         print(request.user.myfoodgroups.All_veggies)
#         # Prepare food data
#         food_data = {
#             'Categories': ['Veggies', 'Beans', 'Fruits', 'Protein', 'Dairy', 'Grains'],
#             'Your Intake': [myfoodgroups.All_veggies, myfoodgroups.Beans_Lentils, myfoodgroups.Fruits_Berries, 
#                            myfoodgroups.Protein, myfoodgroups.Dairy, myfoodgroups.Grains],
#             'USDA': [2.5, 1.5, 2.0, 5.0, 3.0, 3.0]
#         }
        
#         food_df = pd.DataFrame(food_data)
#         # food_df = food_df.astype(str)
#         food_df = food_df.melt(id_vars='Categories', var_name='Source', value_name='Intake')
#         # print(food_df.Intake.dtypes)
       

#         # Prepare fitness data
#         fitness_data = {
#             'Categories': ['Moderate', 'Vigorous', 'Muscle', 'Balance'],
#             'Your Duration': [myfitness.moderate_intensity, myfitness.vigorous_intensity, 
#                              myfitness.muscle_build, myfitness.balance],
#             'HHS': [300, 75, 100, 100]
#         }
#         fitness_df = pd.DataFrame(fitness_data)
#         fitness_df = fitness_df.melt(id_vars='Categories', var_name='Source', value_name='Duration')

#         # Create Seaborn plots
#         sns.set_theme(style="whitegrid")
#         fig, axes = plt.subplots(2, 1, figsize=(4.8, 4), gridspec_kw={'hspace': 0.8})
#         # fig, axes = plt.subplots(2, 1, figsize=(5, 4), sharex=True)

#         sns.barplot(x='Categories', y='Intake', hue='Source', data=food_df, palette=["#377eb8", "#e41a1c"], ax=axes[0], edgecolor='white', width=0.75)
#         axes[0].set_ylabel('Cup Servings', fontsize=8)
#         axes[0].set_title('Food Intake vs. USDA', fontsize=10)
#         axes[0].tick_params(axis='x', labelsize=7)
#         axes[0].legend(fontsize=7)
        
#         # axes[0].set_xticklabels([])
#         axes[0].set_xticklabels([label.get_text().replace('Categories', '') for label in axes[0].get_xticklabels()])
#         axes[0].grid(False)
#         axes[0].set_xlabel('')

#         sns.barplot(x='Categories', y='Duration', hue='Source', data=fitness_df, palette=["#1f77b4", "#9467bd"], ax=axes[1], edgecolor='white', width=0.85)
#         axes[1].set_ylabel('Minutes', fontsize=8)
#         axes[1].set_title('Fitness Duration vs. HHS', fontsize=10)
#         axes[1].tick_params(axis='x', labelsize=7)
#         axes[1].legend(fontsize=7)
#         axes[1].set_xlabel('')
#         for ax in axes:
#             for spine in ax.spines.values():
#                 spine.set_linewidth(1) 
#             ax.spines['top'].set_visible(True)
#             ax.spines['right'].set_visible(True)
#             ax.spines['bottom'].set_visible(True)
#             ax.spines['left'].set_visible(True)
  

#         axes[1].grid(False)
#         for ax in axes:
#             for spine in ax.spines.values():
#                 spine.set_linewidth(0.2) 

#         # axes[0].set_position([0.2, 0.55, 0.8, 0.4])  # Adjust position if needed
#         # axes[1].set_position([0.2, 0.05, 0.8, 0.4])        

#         plt.tight_layout()
#         gridspec_kw={'hspace': 0.8}

#         # Convert plot to image
#         buf = io.BytesIO()
#         plt.savefig(buf, format='png')
#         plt.close()
#         image_data = base64.b64encode(buf.getvalue()).decode('utf-8')

#         return render(request, 'landing-bootstrap.html', {'image_data': image_data})

#     except (Myfoodgroups.DoesNotExist, Myfitness.DoesNotExist):
#         return render(request, 'missing_data.html')


# def DailylogView(request):
#   form=MydailylogForm(request.POST or None)
#   if form.is_valid():
#      try:
#              myfitness_record = user.myfitness
#              moderate_intensity = myfitness_record.moderate_intensity if myfitness_record else None
#              vigorous_intensity = myfitness_record.vigorous_intensity if myfitness_record else None
#              muscle_build = myfitness_record.muscle_build if myfitness_record else None
#              balance = myfitness_record.balance if myfitness_record else None
#      except Myfitness.DoesNotExist:       

#        user_data.append({
#             'moderate_intensity': moderate_intensity,
#             'vigorous_intensity': vigorous_intensity,
#             'muscle_build': muscle_build,
#             'balance': balance,
#         })  
#     obj = form.save(commit=False)
#     print(request.user.id)
#     # print(obj.user.id)
#     study = Study.objects.all()
#     print(f"study: {study.customuser.id}")
#     obj.customuser_id=(request.user.id)
#     obj.save()
    
#     # print (Customuser.Regular_or_Study_Mode)
#     return redirect('landing')
     
#   print(form.errors)
  
#   context = {
#          'form': form,
#           'study': Study,
#           'myfitness': myfitness
#      }
#   template_name = 'food_log2.html'
#   return render(request, 'food_log2.html', context=context)

# def DailylogView(request):
#     User = get_user_model()
#     if isinstance(request.user, User):  # Check if it's your custom user model
#         current_user = request.user
#     else:
#         current_user = User.objects.get(pk=request.user.pk) # Get the CustomUser instance

#     print(current_user)
#     current_user = CustomUser.objects.get(id=request.user.id) 
#     print(current_user)
#     if request.user.is_authenticated:
         
#          print("now printing request.user")
#          print(request.user)
#     form = MydailylogForm(request.POST or None)
#     moderate_intensity = None
#     vigorous_intensity = None
#     muscle_build = None
#     balance = None
#     if form.is_valid():
#         try:
#             myfitness_record = request.user.myfitness 
#             moderate_intensity = myfitness_record.moderate_intensity if myfitness_record else None
#             vigorous_intensity = myfitness_record.vigorous_intensity if myfitness_record else None
#             muscle_build = myfitness_record.muscle_build if myfitness_record else None
#             balance = myfitness_record.balance if myfitness_record else None
#             print(moderate_intensity)
#         except Myfitness.DoesNotExist:
#             # Handle the case where Myfitness record doesn't exist
#             user_data.append({  # Assuming user_data is defined somewhere 
#                 'moderate_intensity': moderate_intensity,
#                 'vigorous_intensity': vigorous_intensity,
#                 'muscle_build': muscle_build,
#                 'balance': balance,
#             }) 
#         obj = form.save(commit=False)
#         obj.customuser_id = request.user.id 
#         obj.save()
#         print(moderate_intensity)
        
#         # print (Customuser.Regular_or_Study_Mode) 
#         return redirect('landing')
    
#     print(form.errors)
    
#     context = {
#         'form': form,
#         # 'study': Study,  # Assuming Study is a model, use Study.objects.all() 
#         # 'study': Study.objects.all(), 
#         'myfitness': Myfitness  # Assuming myfitness is defined 
        
#         # 'user': user,
#     }
#     template_name = 'food_log2.html'
#     return render(request, template_name, context=context)


# @login_required
# def health_dashboard(request):
#     try:
#         myfoodgroups = request.user.myfoodgroups
#         myfitness = request.user.myfitness
#         myexpenses = request.user.myexpenses

#         # Prepare food data
#         food_data = {
#             'Categories': ['Veggies', 'Beans', 'Fruits', 'Protein', 'Dairy', 'Grains'],
#             'Your Intake': [myfoodgroups.All_veggies, myfoodgroups.Beans_Lentils, myfoodgroups.Fruits_Berries, 
#                            myfoodgroups.Protein, myfoodgroups.Dairy, myfoodgroups.Grains],
#             'USDA': [2.5, 1.5, 2.0, 5.0, 3.0, 3.0]
#         }
#         food_df = pd.DataFrame(food_data)
#         food_df = food_df.melt(id_vars='Categories', var_name='Source', value_name='Intake')

#         # Prepare fitness data
#         fitness_data = {
#             'Categories': ['Moderate', 'Vigorous', 'Muscle', 'Balance'],
#             'Your Duration': [myfitness.moderate_intensity, myfitness.vigorous_intensity, 
#                              myfitness.muscle_build, myfitness.balance],
#             'HHS': [300, 75, 60, 100]
#         }
#         fitness_df = pd.DataFrame(fitness_data)
#         fitness_df = fitness_df.melt(id_vars='Categories', var_name='Source', value_name='Duration')

#         # Prepare weekly expense data
#         weekly_expense_data = {
#             'Category': ['Eat Out', 'Groceries', 'Misc.', ],
#             'Cost': [
#                 myexpenses.weekly_eatout_cost, 
#                 myexpenses.weekly_grocery_cost, 
#                 myexpenses.Misc_expenses, 
                
#             ]
#         }
#         weekly_expense_df = pd.DataFrame(weekly_expense_data)

#         # Prepare monthly expense data (assuming some mapping to monthly values)
#         monthly_expense_data = {
#             'Category': ['Insurance', 'Office Visit', 'Prescriptions', 'OOP', 'Gym'],
#             'Cost': [
#                 # Calculate monthly eat out cost (example)
                 
#                 # Calculate monthly grocery cost (example)
                
#                   # Adjust as needed
#                 myexpenses.insurance_premium,  # Assuming monthly
#                 myexpenses.office_visit_cost,  # Adjust as needed
#                 myexpenses.prescription_cost,  # Adjust as needed
#                 myexpenses.oop_cost,  # Adjust as needed
#                 myexpenses.gym_cost 
#             ]
#         }
#         monthly_expense_df = pd.DataFrame(monthly_expense_data)

#         # Create Seaborn plots
#         sns.set_theme(style="white")  # Set style to 'white' to remove gridlines
#         fig, axes = plt.subplots(2, 2, figsize=(10, 6), gridspec_kw={'hspace': 0.5, 'wspace': 0.3}) 

#         # Food Plot
#         sns.barplot(x='Categories', y='Intake', hue='Source', data=food_df, palette=["#377eb8", "#e41a1c"], ax=axes[0, 0], edgecolor='black')
#         axes[0, 0].set_ylabel('Cup Servings', fontsize=8)
#         axes[0, 0].set_title('Food Intake vs. USDA', fontsize=10)
#         axes[0, 0].tick_params(axis='x', labelsize=7)
#         axes[0, 0].legend(fontsize=7)
#         axes[0, 0].set_xlabel('')  # Remove x-axis label
#         for spine in axes[0, 0].spines.values():
#             spine.set_linewidth(0.1) 

#         # Fitness Plot
#         sns.barplot(x='Categories', y='Duration', hue='Source', data=fitness_df, palette=["#1f77b4", "#9467bd"], ax=axes[1, 0], edgecolor='black')
#         axes[1, 0].set_ylabel('Minutes', fontsize=8)
#         axes[1, 0].set_title('Fitness Duration vs. HHS', fontsize=10)
#         axes[1, 0].tick_params(axis='x', labelsize=7)
#         axes[1, 0].legend(fontsize=7)
#         axes[1, 0].set_xlabel('')  # Remove x-axis label
#         for spine in axes[1, 0].spines.values():
#             spine.set_linewidth(0.1)

#         # Weekly Expenses Pie Chart
#         axes[0, 1].pie(weekly_expense_df['Cost'], labels=weekly_expense_df['Category'], autopct='%1.1f%%', startangle=90)
#         axes[0, 1].set_title('Weekly Expenses')

#         # Monthly Expenses Pie Chart
#         axes[1, 1].pie(monthly_expense_df['Cost'], labels=monthly_expense_df['Category'], autopct='%1.1f%%', startangle=90)
#         axes[1, 1].set_title('Monthly Expenses')

#         plt.tight_layout()

#         # Convert plot to image
#         buf = io.BytesIO()
#         plt.savefig(buf, format='png')
#         plt.close()
#         image_data = base64.b64encode(buf.getvalue()).decode('utf-8')

#         return render(request, 'landing-bootstrap.html', {'image_data': image_data})

#     except (Myfoodgroups.DoesNotExist, Myfitness.DoesNotExist, Myexpenses.DoesNotExist):
#         return render(request, 'missing_data.html') 

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

# class LoginView(TemplateView):
#   success_url = reverse_lazy('landing')
#   template_name = 'login.html'

# class MyLoginView(LoginView):
#     template_name = 'registration/login.html'

#     def form_valid(self, form):
#         user = form.get_user()
#         print(user.last_login)
#         if user.is_superuser or user.is_staff:
#             return redirect('admin:index') 
#         elif not user.last_login:
#             return redirect('myfoodgroups')
#         else:
#             return redirect('landing')            

# Clean this up, ensure that more dieticians can be added in the future