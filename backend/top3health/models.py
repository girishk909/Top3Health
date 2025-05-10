from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
import datetime as dt
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.conf import settings
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.contrib.auth.models import Group, Permission
from django.contrib import admin
from datetime import date
# from django.contrib.auth.admin import UserAdmin
# from .models import CustomUser

# Create your models here.

from django.core.validators import RegexValidator
# from django.contrib.localflavor.us.models import USStateField

class CustomUser(AbstractUser):
  username = models.CharField(max_length=14, null=False, blank=False, unique=True,)
  first_name = models.CharField(max_length=300, null=False, blank=False)
  last_name = models.CharField(max_length=300, null=False, blank=False)
  Height_ft = models.IntegerField(null=True, blank=False)
  Height_in = models.IntegerField(null=True, blank=False)
  Weight_in_pounds = models.IntegerField(null=True, blank=False)
  Gender = models.CharField(max_length=10, null=True, blank=True)
  role = models.CharField(max_length=20, choices=[('dietician', 'Dietician'), ('director', 'Director'), ('custom_admin', 'Custom_admin'),('user', 'User')], default='user')
  mode = models.CharField(max_length=10, choices=[('regular', 'Regular'), ('study_mode', 'Study_mode')], default='regular', blank=True, null=False)
  study_type =  models.CharField(max_length=10, choices=[('diabetes', 'Diabetes'), ('cvd', 'Cvd')],  blank=True, null=False)
  middle_initial = models.CharField(max_length=1, null=True, blank = True)
  address_1 = models.CharField(max_length = 100, null=False, blank=False)
  address_2 = models.CharField(max_length = 30, null=True, blank=True)
  zipcode = models.CharField(max_length = 5, null=False, blank=False,)
  city = models.CharField(max_length = 100, null=False, blank=False,)
  state = models.CharField(max_length = 50, null=False, blank=False,)
  phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
  phone_number = models.CharField(validators=[phone_regex], max_length=17, null=False, blank=False,) # Validators should be a list
#   email = models.EmailField(max_length=254, null=False, blank=False)
  dob = models.CharField(max_length=10,null=True, blank=False,)
  

  def __int__(self):
        return self.customuser
      
class Dietician(models.Model):

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    license_number  = models.CharField(max_length=20, blank=True)

def create_dietician_user(username, first_name, last_name, email, password): 
    user = User.objects.create_user(username=username, first_name=first_name, last_name= last_name, email=email, password=password)
    user.is_staff = True 
    user.save()

    dietician_group, created = Group.objects.get_or_create(name='dietician') 
    user.groups.add(dietician_group) 

    # Create a corresponding Dietician instance
    Dietician.objects.create(user=user) 

    return user

class Study(models.Model):
    customuser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # mode = models.CharField(max_length=10, choices=[('regular', 'Regular'), ('study_mode', 'Study_mode')], default='regular', blank=True, null=False)
    study_topic = models.CharField(max_length=20, choices=[('diabetes', 'Diabetes'), ('cardiovascular', 'Cardiovascular')], blank=True, null=True)      
     
     
    def __int__(self):
        return self.customuser       

class Dietician_note(models.Model):

    customuser = models.OneToOneField(CustomUser,null=False,  primary_key=True, on_delete= models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now,null=True, blank=True )

    note1 = models.CharField(max_length=50, null=True,blank=True)
    note2 = models.CharField(max_length=50, null=True,blank=True)
    note3 = models.CharField(max_length=50, null=True,blank=True)
    note4 = models.CharField(max_length=50, null=True,blank=True)
    note5 = models.CharField(max_length=50, null=True,blank=True)
    note6 = models.CharField(max_length=50, null=True,blank=True)
    note7 = models.CharField(max_length=50, null=True,blank=True)
    note8 = models.CharField(max_length=50, null=True,blank=True)
    note9 = models.CharField(max_length=50, null=True,blank=True)
    note10 = models.CharField(max_length=50, null=True,blank=True)

    def __int__(self):
        return self.customuser 

class Mydailylog(models.Model):

    customuser = models.ForeignKey(CustomUser,   on_delete= models.CASCADE)
    date = models.DateField(null=False, blank=False) 
    
    Breakfast_name = models.CharField(max_length=50, null=True,blank=True,)
    Breakfast_description = models.CharField(max_length=250, null=True,blank=True,)

    Lunch_name = models.CharField(max_length=50, null=True,blank=True,)
    Lunch_description = models.CharField(max_length=250, null=True,blank=True,)

    Dinner_name = models.CharField(max_length=50, null=True,blank=True,)
    Dinner_description = models.CharField(max_length=250, null=True,blank=True,)
    
    veggies = models.IntegerField(null=False, blank=False)
    beans_lentils = models.IntegerField(null=False, blank=False)
    fruits_berries = models.IntegerField(null=False, blank=False)
    dairy = models.IntegerField(null=False, blank=False) 
    grains = models.IntegerField(null=False, blank=False)
    protein = models.IntegerField(null=False, blank=False)

    moderate_intensity_type = models.CharField(max_length=50, null=True,blank=True,)
    moderate_intensity = models.IntegerField(null=True, blank=True)
    vigorous_intensity_type = models.CharField(max_length=50, null=True,blank=True,)
    vigorous_intensity = models.IntegerField(null=True, blank=True)
    muscle_build_type = models.CharField(max_length=50, null=True,blank=True,)
    muscle_build = models.IntegerField(null=True, blank=True)
    balance_type = models.CharField(max_length=50, null=True,blank=True,)
    balance = models.IntegerField(null=True, blank=True)
   
    Stretches = models.CharField(max_length=50, null=True,blank=True,)
    Stretch_check = models.BooleanField(default=False)
    Reduce_processed = models.CharField(max_length=50, null=True,blank=True,)
    Reduce_processed_check = models.BooleanField(default=False)
    Prepare_meals = models.CharField(max_length=50, null=True,blank=True,)
    Prepare_meals_check = models.BooleanField(default=False)
    Wake_time = models.CharField(max_length=50, null=True,blank=True,)
    Wake_time_check = models.BooleanField(default=False)
    food_cost_savings = models.CharField(max_length=50, null=True,blank=True,)
    food_savings_check = models.BooleanField(default=False)
    Clear_kitchen = models.CharField(max_length=50, null=True,blank=True)
    Clear_kitchen_check = models.BooleanField(default=False)
    Brush_Floss = models.CharField(max_length=50, null=True,blank=True)
    Brush_Floss_check = models.BooleanField(default=False)
    Groceries_shop = models.CharField(max_length=30, null=True,blank=True)
    Groceries_shop_check = models.BooleanField(default=False)
    daily_mindfulness = models.CharField(max_length=50, null=True,blank=True,)
    daily_mindfulness_check = models.BooleanField(default=False)
    food_suggestions = models.CharField(max_length=50, null=True,blank=True,)
    food_suggestions_check = models.BooleanField(default=False)
    reduce_alcohol = models.CharField(max_length=50, null=True,blank=True,)
    reduce_alcohol_check = models.BooleanField(default=False)
    reduce_smoking = models.CharField(max_length=50, null=True,blank=True,)
    reduce_smoking_check = models.BooleanField(default=False)

    custom_habit_1 = models.CharField(max_length=50, null=True,blank=True,)
    custom_habit_1_check = models.BooleanField(default=False)
    custom_habit_2 = models.CharField(max_length=50, null=True,blank=True,)
    custom_habit_2_check = models.BooleanField(default=False)
    custom_habit_3 = models.CharField(max_length=50, null=True,blank=True,)
    custom_habit_3_check = models.BooleanField(default=False)  

    daily_eatout_cost =  models.IntegerField(null=True, blank=True)
    daily_misc_cost = models.IntegerField(null=True, blank=True)
    daily_grocery_cost = models.IntegerField(null=True, blank=True)


    def __int__(self):
        return self.customuser           

class Myhealthscreening(models.Model):
    customuser = models.ForeignKey(CustomUser, on_delete= models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now,null=True, blank=True )
    Blood_glucose = models.CharField(max_length=4, null=True, blank=True)

    A1C = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    BP_systolic = models.IntegerField(null=True, blank=True, default=None)
    BP_diastolic = models.IntegerField(null=True, blank=True, default=None)
    Total_Cholesterol = models.IntegerField(null=True, blank=True, default=None)
    HDL = models.IntegerField(null=True, blank=True, default=None)
    LDL = models.IntegerField(null=True, blank=True, default=None)
    Triglycerides = models.IntegerField(null=True, blank=True, default=None)
    Smoker = models.CharField(max_length=3, null=True, blank=True, default=None)
    Blood_type = models.CharField(max_length=3, blank=True, null=True, default=None)

    # Dental_checkups = models.BooleanField(default=False)
    # Dental_cleanings = models.BooleanField(default=False)

    dental_date = models.DateField(max_length=10,null=True, blank=True,)
    vision_date = models.DateField(max_length=10,null=True, blank=True,)

    # Vision_checkups = models.BooleanField(default=False)
    Screen_date = models.DateField(max_length=10,null=True, blank=True,)
   
   
    def __int__(self):
        return self.customuser   


class Healthsym(models.Model):
    customuser = models.ForeignKey(CustomUser, on_delete= models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now,null=True, blank=True )

    Minor1 = models.CharField(max_length=30,null=True, blank=True)
    Minor2 = models.CharField(max_length=30,null=True, blank=True)
    Minor3 = models.CharField(max_length=30,null=True, blank=True)

    Minor4 = models.CharField(max_length=30,null=True, blank=True)
    Minor5 = models.CharField(max_length=40,null=True, blank=True)

    Major1 = models.CharField(max_length=20,null=True, blank=True)
    Major2 = models.CharField(max_length=20,null=True, blank=True)
    Major3 = models.CharField(max_length=20,null=True, blank=True)
   

    Major4 = models.CharField(max_length=30,null=True,blank=True)
    Major5 = models.CharField(max_length=30,null=True, blank=True)

    physical_health = models.CharField(max_length=20,null=True,blank=True)
    mental_health = models.CharField(max_length=20,null=True,blank=True)
    social_relations = models.CharField(max_length=20,null=True,blank=True)
    access_health_food = models.CharField(max_length=20,null=True,blank=True)

    def __int__(self):
        return self.customuser


class Myfitness(models.Model):

    customuser = models.OneToOneField(CustomUser, null=False, primary_key=True, on_delete= models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now,null=True, blank=True )
    moderate_intensity = models.IntegerField(null=True,blank=True, default=0)
    vigorous_intensity = models.IntegerField(null=True,blank=True, default=0)
    muscle_build = models.IntegerField(null=True,blank=True, default=0)
    balance = models.IntegerField(null=True,blank=True, default=0)

    def __int__(self):
        return self.customuser  

class Myfoodgroups(models.Model):
    customuser = models.OneToOneField(CustomUser, primary_key=True, on_delete= models.CASCADE, related_name='myfoodgroups')
    created_at = models.DateTimeField(default=timezone.now,null=True, blank=True )
    All_veggies = models.IntegerField(null=False,blank=False)
    # Red_Orange_veggies = models.IntegerField(null=True,blank=True)
    Beans_Lentils = models.IntegerField(null=False,blank=False)
    # Other_veggies = models.IntegerField(null=True,blank=True)
    Fruits_Berries = models.IntegerField(null=False,blank=False)
    Protein = models.IntegerField(null=False,blank=False)
    Dairy = models.IntegerField(null=False,blank=False)
    Grains =models.IntegerField(null=False,blank=False)

    Allergic1 = models.CharField(max_length=30,  null=True,blank=True)
    Substitute1 = models.CharField(max_length=30,  null=True,blank=True)
    Allergic2 = models.CharField(max_length=30,  null=True,blank=True)
    Substitute2 = models.CharField(max_length=30,  null=True,blank=True)
    Allergic3 = models.CharField(max_length=30,  null=True,blank=True)
    Substitute3 = models.CharField(max_length=30,  null=True,blank=True)
    # Allergic4 = models.CharField(max_length=30,  null=True,blank=True)
    # Substitute4 = models.CharField(max_length=30,  null=True,blank=True)
    # Herbs_Spices = models.IntegerField(null=True,blank=True)

    def __int__(self):
        return self.customuser
       
class Myfoodsuggestions(models.Model):
    customuser = models.OneToOneField(CustomUser, null=False, primary_key=True, on_delete= models.CASCADE)
    Salads = models.CharField(max_length=16,  )
    Sandwiches = models.CharField(max_length=16,  )
    Fruits_Berries = models.CharField(max_length=16,  )
    Dairy = models.CharField(max_length=16,  )
    Pasta = models.CharField(max_length=16,  )
    Egg_based = models.CharField(max_length=16,  )
    Grains = models.CharField(max_length=16, )
    Soups =  models.CharField(max_length=16, )
    Oats =  models.CharField(max_length=16,  )
    Beans_Legumes =  models.CharField(max_length=16,  )
    Smoothies = models.CharField(max_length=16, )
    Tacos_Burritos = models.CharField(max_length=16, )
    # Rice_based = models.CharField(max_length=16, )
    Nuts_Seeds = models.CharField(max_length=16,  )
    Roti = models.CharField(max_length=16,  )

    def __int__(self):
        return self.customuser  

class Myallergicfoods(models.Model):
    customuser = models.OneToOneField(CustomUser, null=False, primary_key=True, on_delete= models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now,null=True, blank=True )
    allergicFood1 = models.CharField(max_length=16,  null=True,blank=True)
    allergicFood2 = models.CharField(max_length=16,  null=True,blank=True)
    allergicFood3 = models.CharField(max_length=16,  null=True,blank=True)
    allergicFood4 = models.CharField(max_length=16,  null=True,blank=True)
    allergicFood5 = models.CharField(max_length=16,  null=True,blank=True)
    allergicFood6 = models.CharField(max_length=16,  null=True,blank=True)
    allergicFood7 = models.CharField(max_length=16,  null=True,blank=True)
    allergicFood8 = models.CharField(max_length=16,  null=True,blank=True)

    Food_substitute_1 = models.CharField(max_length=16,  null=True,blank=True)
    Food_substitute_2 = models.CharField(max_length=16,  null=True,blank=True)
    Food_substitute_3 = models.CharField(max_length=16,  null=True,blank=True)
    Food_substitute_4 = models.CharField(max_length=16,  null=True,blank=True)
    Food_substitute_5 = models.CharField(max_length=16,  null=True,blank=True)
   
    def __int__(self):
        return self.customuser        

class Mytypmeals1(models.Model):

    customuser = models.ForeignKey(CustomUser, on_delete= models.CASCADE)
    
    created_at = models.DateTimeField(default=timezone.now,null=True, blank=True )
    BCuisine1 = models.CharField(max_length=50, null=True,blank=True)
    B1_freq = models.CharField(max_length=16,  null=True, blank=True)
    Breakfast1 = models.CharField(max_length=50, null=True,blank=True)
    
    IngredientB11 = models.CharField(max_length=50, null=True,blank=True)    
    IngredientB12 = models.CharField(max_length=50, null=True,blank=True)
    IngredientB13 = models.CharField(max_length=50, null=True,blank=True)
    IngredientB14 = models.CharField(max_length=50, null=True,blank=True)

    IngredientB15 = models.CharField(max_length=50, null=True,blank=True)    
    IngredientB16 = models.CharField(max_length=50, null=True,blank=True)
    IngredientB17 = models.CharField(max_length=50, null=True,blank=True)
    IngredientB18 = models.CharField(max_length=50, null=True,blank=True)

    Ingredientbdr11 = models.CharField(max_length=50, null=True,blank=True)    
    Ingredientbdr12 = models.CharField(max_length=50, null=True,blank=True)
    Ingredientbdr13 = models.CharField(max_length=50, null=True,blank=True)
    Ingredientbdr14 = models.CharField(max_length=50, null=True,blank=True)

    LCuisine1 = models.CharField(max_length=50, null=True,blank=True)
    L1_freq = models.CharField(max_length=16, null=True, blank=True)
    Lunch1 = models.CharField(max_length=50, null=True,blank=True)

    IngredientL11 = models.CharField(max_length=50, null=True,blank=True)    
    IngredientL12 = models.CharField(max_length=50, null=True,blank=True)
    IngredientL13 = models.CharField(max_length=50, null=True,blank=True)
    IngredientL14 = models.CharField(max_length=50, null=True,blank=True)

    IngredientL15 = models.CharField(max_length=50, null=True,blank=True)    
    IngredientL16 = models.CharField(max_length=50, null=True,blank=True)
    IngredientL17 = models.CharField(max_length=50, null=True,blank=True)
    IngredientL18 = models.CharField(max_length=50, null=True,blank=True)

    Ingredientldr11 = models.CharField(max_length=50, null=True,blank=True)    
    Ingredientldr12 = models.CharField(max_length=50, null=True,blank=True)
    Ingredientldr13 = models.CharField(max_length=50, null=True,blank=True)
    Ingredientldr14 = models.CharField(max_length=50, null=True,blank=True)

    DCuisine1 = models.CharField(max_length=50, null=True,blank=True)
    D1_freq = models.CharField(max_length=16,  null=True, blank=True)
    Dinner1 = models.CharField(max_length=50, null=True,blank=True)

    IngredientD11 = models.CharField(max_length=50, null=True,blank=True)    
    IngredientD12 = models.CharField(max_length=50, null=True,blank=True)
    IngredientD13 = models.CharField(max_length=50, null=True,blank=True)
    IngredientD14 = models.CharField(max_length=50, null=True,blank=True)

    IngredientD15 = models.CharField(max_length=50, null=True,blank=True)    
    IngredientD16 = models.CharField(max_length=50, null=True,blank=True)
    IngredientD17 = models.CharField(max_length=50, null=True,blank=True)
    IngredientD18 = models.CharField(max_length=50, null=True,blank=True)

    Ingredientddr11 = models.CharField(max_length=50, null=True,blank=True)    
    Ingredientddr12 = models.CharField(max_length=50, null=True,blank=True)
    Ingredientddr13 = models.CharField(max_length=50, null=True,blank=True)
    Ingredientddr14 = models.CharField(max_length=50, null=True,blank=True)

    Snack1 = models.CharField(max_length=50, null=True,blank=True)
    Snack1_freq = models.CharField(max_length=16,  null=True, blank=True)

    Snack2 = models.CharField(max_length=50, null=True,blank=True)
    Snack2_freq = models.CharField(max_length=16,  null=True, blank=True)

    Water_intake = models.CharField(max_length=50, null=True,blank=True)
   
    def __int__(self):
        return self.customuser        
       
class Myexpenses(models.Model):

        customuser = models.OneToOneField(CustomUser, null=False, primary_key=True, on_delete= models.CASCADE)
        created_at = models.DateTimeField(default=timezone.now,null=True, blank=True )
        family_eatout_count  = models.IntegerField(null=True, blank=True)
        weekly_eatout_cost  = models.IntegerField(null=True, blank=True)
        family_grocery_count  = models.IntegerField(null=True, blank=True)
        weekly_grocery_cost  = models.IntegerField(null=True, blank=True)
        Misc_expense_member  = models.IntegerField(null=True, blank=True)
        Misc_expenses  = models.IntegerField(null=True, blank=True)
        family_premium_count  = models.IntegerField(null=True, blank=True)
        insurance_premium  = models.IntegerField(null=True, blank=True)
        members_for_office_visit  = models.IntegerField(null=True, blank=True)
        office_visit_cost  = models.IntegerField(null=True, blank=True)
        members_for_prescriptions  = models.IntegerField(null=True, blank=True)
        prescription_cost  = models.IntegerField(null=True, blank=True)
        members_for_oop  = models.IntegerField(null=True, blank=True)
        oop_cost  = models.IntegerField(null=True, blank=True)
        members_for_gym  = models.IntegerField(null=True, blank=True)
        gym_cost  = models.IntegerField(null=True, blank=True)

        def __int__(self):
          return self.customuser

class Mymonthlyexpenses(models.Model):

        customuser = models.ForeignKey(CustomUser, on_delete= models.CASCADE)
        created_at = models.DateTimeField(default=timezone.now,null=True, blank=True )
       
        family_premium_count  = models.IntegerField(null=True, blank=True)
        insurance_premium  = models.IntegerField(null=True, blank=True)
        members_for_office_visit  = models.IntegerField(null=True, blank=True)
        office_visit_cost  = models.IntegerField(null=True, blank=True)
        members_for_prescriptions  = models.IntegerField(null=True, blank=True)
        prescription_cost  = models.IntegerField(null=True, blank=True)
        members_for_oop  = models.IntegerField(null=True, blank=True)
        oop_cost  = models.IntegerField(null=True, blank=True)
        members_for_gym  = models.IntegerField(null=True, blank=True)
        gym_cost  = models.IntegerField(null=True, blank=True)

        def __int__(self):
          return self.customuser          

class Supplements(models.Model):
          
    customuser = models.ForeignKey(CustomUser, on_delete= models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now,null=True, blank=True )
    Supplement_1 = models.CharField(max_length=100, null=True, blank=True,unique=True)
    Supplement_2 = models.CharField(max_length=100, null=True, blank=True,unique=True)
    Supplement_3 = models.CharField(max_length=100, null=True, blank=True,unique=True)
    Supplement_4 = models.CharField(max_length=100, null=True, blank=True,unique=True)
    Supplement_5 = models.CharField(max_length=100, null=True, blank=True,unique=True)          

class Myhabits(models.Model):   
        customuser = models.ForeignKey(CustomUser, on_delete= models.CASCADE,related_name='myhabits')
        created_at = models.DateTimeField(default=timezone.now,null=True, blank=True )
        Stretches = models.CharField(max_length=50, null=True,blank=True,)
        Reduce_processed = models.CharField(max_length=50, null=True,blank=True,)
        Prepare_meals = models.CharField(max_length=50, null=True,blank=True,)
        Wake_time = models.CharField(max_length=50, null=True,blank=True,)
        food_cost_savings = models.CharField(max_length=50, null=True,blank=True,)
        Clear_kitchen = models.CharField(max_length=50, null=True,blank=True)
        Brush_Floss = models.CharField(max_length=50, null=True,blank=True)
        Groceries_shop = models.CharField(max_length=30, null=True,blank=True)
        daily_mindfulness = models.CharField(max_length=50, null=True,blank=True,)
        food_suggestions = models.CharField(max_length=50, null=True,blank=True,)
        reduce_alcohol = models.CharField(max_length=50, null=True,blank=True,)
        reduce_smoking = models.CharField(max_length=50, null=True,blank=True,)

        custom_habit_1 = models.CharField(max_length=50, null=True,blank=True,)
        custom_habit_2 = models.CharField(max_length=50, null=True,blank=True,)
        custom_habit_3 = models.CharField(max_length=50, null=True,blank=True,)

        # Mindful_yoga = models.BooleanField(default=False)
        # Weekly_suggestions = models.BooleanField(default=False)
        # Weekly_feedback = models.BooleanField(default=False)

        # Daily_habit_1 = models.CharField(max_length=30,  null=True,blank=True, unique=True)
        # Daily_habit_2 = models.CharField(max_length=30,  null=True,blank=True, unique=True)
        # Weekly_habit_1 = models.CharField(max_length=30,  null=True,blank=True, unique=True)
        # Weekly_habit_2 = models.CharField(max_length=30,  null=True,blank=True, unique=True)

        def __int__(self):
          return self.customuser
        
class Beginpage(models.Model):
    customuser = models.ForeignKey(CustomUser, on_delete= models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now,null=True, blank=True )
    begin_date = models.DateField(max_length=10,null=True, blank=True,)
    daily_log_time = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    weekly_log_time = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    weekly_suggestion_time = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)


class Foods(models.Model):
    Food_name = models.CharField(max_length=50, null=True, blank=True)
    Quantity = models.DecimalField(max_digits = 5, decimal_places = 2, null=True, blank=True)
    Measure = models.CharField(max_length=10, null=True, blank=True)
    Weight = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Unit = models.CharField(max_length=10, null=True, blank=True)
    Prep = models.CharField(max_length=10, null=True, blank=True)
   
    GI = models.CharField(max_length=10,null=True, blank=True)
    Water = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Water_DV = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Energy = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Energy_DV = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Protein = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Protein_DV = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Total_lipid = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Total_lipid_DV = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)

    Carbs = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Carbs_DV = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Fiber = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Fiber_DV = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Sugars = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Sugars_DV = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Boron = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Boron_DV = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)

    Calcium = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Calcium_DV = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Chloride = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Chloride_DV = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Chromium = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Chromium_DV = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Copper = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Copper_DV = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    
    Fluoride = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Fluoride_DV = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Iodine = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Iodine_DV = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Iron = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Iron_DV = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Magnesium = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Magnesium_DV = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)

    Manganese = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Manganese_DV = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Molybdenum = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Molybdenum_DV = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Phosphorus = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Phosphorus_DV = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Potassium = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Potassium_DV = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)

    Selenium = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Selenium_DV = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Sodium = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Sodium_DV = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Zinc = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Zinc_DV = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Thiamin_B1 = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Thiamin_B1_DV = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)

    Riboflavin_B2 = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Riboflavin_B2_DV = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Niacin_B3 = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Niacin_B3_DV = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Vitamin_B6 = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Vitamin_B6_DV = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Vitamin_B12 = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Vitamin_B12_DV = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Biotin_B7 = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Biotin_B7_DV = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    
    Choline = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Choline_DV = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Folate_B9 = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Folate_B9_DV = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Pantothenic = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Pantothenic_DV = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Vitamin_C = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Vitamin_C_DV = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Vitamin_A_RAE = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Vitamin_A_DV = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)

    Vitamin_D_IU = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Vitamin_D_DV = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Vitamin_E_ATE = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Vitamin_E_DV = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Vitamin_K = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Vitamin_K_DV = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Fatty_acids_total_sat = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Fatty_acids_sat_DV = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Fatty_acids_total_mono = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Fatty_acids_mono_DV = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)

    Fatty_acids_total_poly = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Fatty_acids_poly_DV = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Fatty_acids_total_trans = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Fatty_acids_trans_DV = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Cholesterol = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Cholesterol_DV = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Omega_3 = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Omega_3_DV = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Omega_6 = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)
    Omega_6_DV = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank=True)

    # class Myfastfoods(models.Model):
#     customuser = models.OneToOneField(CustomUser, null=False, primary_key=True, on_delete= models.CASCADE)
#     Bacon = models.CharField(max_length=16,  null=False,blank=False)
#     Burgers = models.CharField(max_length=16,  null=False,blank=False)
#     Cookies = models.CharField(max_length=16,  null=False,blank=False)
#     Cereals = models.CharField(max_length=16,  null=False,blank=False)
#     # Canned_foods = models.CharField(max_length=16,  null=False,blank=False, unique=True)
#     Frozen_pizza = models.CharField(max_length=16,  null=False,blank=False)
#     Ice_cream = models.CharField(max_length=16,  null=False,blank=False)
#     Pancakes = models.CharField(max_length=16,  null=False,blank=False)
#     Fried_foods = models.CharField(max_length=16,  null=False,blank=False)
#     Popcorn = models.CharField(max_length=16,  null=False,blank=False)
#     # Margarine = models.CharField(max_length=16, null=False,blank=False, unique=True)
#     # Butter = models.CharField(max_length=16,  null=False,blank=False, unique=True)
#     Frozen_meals = models.CharField(max_length=16,  null=False,blank=False)
#     # Regular_pizza = models.CharField(max_length=16, null=False,blank=False, unique=True)
#     French_fries = models.CharField(max_length=16,  null=False,blank=False)
#     Potato_chips = models.CharField(max_length=16,  null=False,blank=False)
#     Soft_drinks = models.CharField(max_length=16,  null=False,blank=False)
#     Milk_shakes = models.CharField(max_length=16,  null=False,blank=False)

#     def __int__(self):
#         return self.customuser  

# def get_default_value():
#     return "user"

# class CustomRole(models.Model):
#     customuser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     role_type = models.CharField(max_length=20, choices=[('dietician', 'Dietician'), ('director', 'Director'), ('custom_admin', 'Custom_admin'),('user', 'User')], default='user', editable='True')   
     
#     def __int__(self):
#         return self.customuser 


# class StaffUser(models.Model):

# #   models.OneToOneField(CustomUser, on_delete=models.CASCADE) 
#   user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#   first_name = models.CharField(max_length=300, null=False, blank=False)
#   last_name = models.CharField(max_length=300, null=False, blank=False)
#   role = models.CharField(max_length=20, choices=[('dietician', 'Dietician'), ('director', 'Director'), ('custom_admin', 'Custom_admin'),])
#   middle_initial = models.CharField(max_length=1, null=True, blank = True)
#   phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
#   phone_number = models.CharField(validators=[phone_regex], max_length=17, null=False, blank=False,) 