from django.contrib.auth.models import AbstractUser
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
  mode = mode = models.CharField(max_length=10, choices=[('regular', 'Regular'), ('study_mode', 'Study_mode')], default='regular', blank=True, null=False)
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
      
class Study(models.Model):
    customuser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # mode = models.CharField(max_length=10, choices=[('regular', 'Regular'), ('study_mode', 'Study_mode')], default='regular', blank=True, null=False)
    study_topic = models.CharField(max_length=20, choices=[('diabetes', 'Diabetes'), ('cardiovascular', 'Cardiovascular')], blank=True, null=True)      
     
     
    def __int__(self):
        return self.customuser       

def get_default_value():
    return "user"

class CustomRole(models.Model):
    customuser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    role_type = models.CharField(max_length=20, choices=[('dietician', 'Dietician'), ('director', 'Director'), ('custom_admin', 'Custom_admin'),('user', 'User')], default='user', editable='True')   
     
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
    
    BS_before_bk = models.IntegerField(null=True, blank=True)
    BS_after_bk = models.IntegerField(null=True, blank=True)

    BS_before_lu = models.IntegerField(null=True, blank=True)
    BS_after_lu = models.IntegerField(null=True, blank=True)

    BS_before_di = models.IntegerField(null=True, blank=True)
    BS_after_di = models.IntegerField(null=True, blank=True)
    
    
    Breakfast1 = models.CharField(max_length=50, null=True,blank=True)
    IngredientB11 = models.CharField(max_length=50, null=True,blank=True)    
    IngredientB12 = models.CharField(max_length=50, null=True,blank=True)
    IngredientB13 = models.CharField(max_length=50, null=True,blank=True)
    IngredientB14 = models.CharField(max_length=50, null=True,blank=True)


    Lunch1 = models.CharField(max_length=50, null=True,blank=True)
    IngredientL11 = models.CharField(max_length=50, null=True,blank=True)    
    IngredientL12 = models.CharField(max_length=50, null=True,blank=True)
    IngredientL13 = models.CharField(max_length=50, null=True,blank=True)
    IngredientL14 = models.CharField(max_length=50, null=True,blank=True)


    Dinner1 = models.CharField(max_length=50, null=True,blank=True)
    IngredientD11 = models.CharField(max_length=50, null=True,blank=True)    
    IngredientD12 = models.CharField(max_length=50, null=True,blank=True)
    IngredientD13 = models.CharField(max_length=50, null=True,blank=True)
    IngredientD14 = models.CharField(max_length=50, null=True,blank=True)

    Fitness_1= models.CharField(max_length=50, null=True,blank=True)
    Fitness_2 = models.CharField(max_length=50, null=True,blank=True)    
   
    Habit_1= models.CharField(max_length=50, null=True,blank=True)
    Habit_2 = models.CharField(max_length=50, null=True,blank=True) 
    Habit_3= models.CharField(max_length=50, null=True,blank=True)
    Habit_4 = models.CharField(max_length=50, null=True,blank=True) 
    Habit_5 = models.CharField(max_length=50, null=True,blank=True)    

    def __int__(self):
        return self.customuser           

class Goals(models.Model):
    # customuser = models.OneToOneField(CustomUser,null=False,  primary_key=True, on_delete= models.CASCADE)
    customuser = models.ForeignKey(CustomUser, on_delete= models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now,null=True, blank=True )
    Become_Healthier = models.BooleanField(default=False)
    Lose_Weight = models.BooleanField(default=False)
    Improve_Productivity = models.BooleanField(default=False)
    Increase_Fitness = models.BooleanField(default=False)
    Reduce_Stress = models.BooleanField(default=False)
    Improve_Sleep = models.BooleanField(default=False)
    Quit_Substances= models.BooleanField(default=False)
    Reduce_fast_foods = models.BooleanField(default=False)
    Improve_Symptoms= models.BooleanField(default=False)
    Reduce_Expenses= models.BooleanField(default=False)
    Use_Habits = models.BooleanField(default=False)
    # Explore_Mindful = models.BooleanField(default=False, unique=True)

    def __int__(self, **kwargs):
        return self.customuser

    # def get_absolute_url(self):
    #     return ('goalsupdate', kwargs=={"pk": self.pk})    
# class Goals_ver(models.Model):
#     customuser = models.ForeignKey(CustomUser, on_delete= models.CASCADE)
#     Become_Healthier = models.BooleanField()
#     Lose_Weight = models.BooleanField(default=False)
#     Maintain_Weight = models.BooleanField(default=False)
#     Gain_Weight = models.BooleanField(default=False)
#     Improve_Productivity = models.BooleanField()
#     Increase_Strength = models.BooleanField()
#     Increase_Endurance = models.BooleanField()
#     Explore_Cuisines = models.BooleanField()
#     Organize_Kitchen = models.BooleanField()
#     Reduce_Stress = models.BooleanField()
#     Improve_Sleep = models.BooleanField()
#     Reduce_fast_foods = models.BooleanField(default=False)
#     Quit_Smoking= models.BooleanField()
#     Quit_Alcohol= models.BooleanField()
#     Include_Yoga = models.BooleanField()
#     # Explore_Mindful = models.BooleanField(default=False, unique=True)

#     def __int__(self, **kwargs):
#         return self.customuser

class MyProfile(models.Model):
    customuser = models.OneToOneField(CustomUser,null=False, primary_key=True, on_delete= models.CASCADE)
    Height_ft = models.IntegerField(null=False, blank=False)
    Height_in = models.IntegerField(null=False, blank=False)
    Weight_in_pounds = models.IntegerField(null=False, blank=False)
    Gender = models.CharField(max_length=10, null=True, blank=True)
    Calories_intake = models.IntegerField(null=True, blank=True, default=None)
    Calories_burned = models.IntegerField(null=True, blank=True, default=None)
    Protein_intake = models.IntegerField(null=True, blank=True, default=None)
    Carbs_intake = models.IntegerField(null=True, blank=True, default=None)
    Water_intake = models.IntegerField(null=False, blank=False)
    Stress_level = models.CharField(max_length=6, null=False, blank=False)
    Sleep_quality = models.CharField(max_length=8, null=False, blank=False)
    Race = models.CharField(max_length=35,null=False, blank=False)
    Ethnicity = models.CharField(max_length=30,null=False, blank=False)
    role = models.CharField(max_length=30,  
    choices=[('admin', 'Admin'), ('dietician', 'Dietician'), ('user', 'User')], default='user')
   
    def __int__(self):
        return self.customuser       

# class MyProfile_ver(models.Model):
#     customuser = models.ForeignKey(CustomUser, on_delete= models.CASCADE)
#     Height_ft = models.IntegerField(null=False, blank=False)
#     Height_in = models.IntegerField(null=False, blank=False)
#     Weight_in_pounds = models.IntegerField(null=False, blank=False)
#     Gender = models.CharField(max_length=10, null=True, blank=True)
#     Calories_intake = models.IntegerField(null=True, blank=True)
#     Calories_burned = models.IntegerField(null=True, blank=True)
#     Protein_intake = models.IntegerField(null=True, blank=True)
#     Carbs_intake = models.IntegerField(null=True, blank=True)
#     Water_intake = models.IntegerField(null=False, blank=False)
#     Stress_level = models.CharField(max_length=6, null=False, blank=False)
#     Sleep_quality = models.CharField(max_length=8, null=False, blank=False)
#     Race = models.CharField(max_length=30,null=False, blank=False)
#     Ethnicity = models.CharField(max_length=30,null=False, blank=False)
    
#     def __int__(self):
#         return self.customuser            

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

    Dental_checkups = models.BooleanField(default=False)
    Dental_cleanings = models.BooleanField(default=False)

    Vision_checkups = models.BooleanField(default=False)
    Screen_date = models.DateField(max_length=10,null=True, blank=True,)
   
   
    def __int__(self):
        return self.customuser   

class Userhealthscreen(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    healthscreen = models.ForeignKey(Myhealthscreening, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


# class Myhealthscreening_ver(models.Model):
#     customuser = models.ForeignKey(CustomUser, on_delete= models.CASCADE)
#     Blood_glucose = models.CharField(max_length=4, null=True, blank=True)
#     A1C = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
#     BP_systolic = models.IntegerField(null=True, blank=True)
#     BP_diastolic = models.IntegerField(null=True, blank=True)
#     Total_Cholesterol = models.IntegerField(null=True, blank=True)
#     HDL = models.IntegerField(null=True, blank=True, default=None)
#     LDL = models.IntegerField(null=True, blank=True, default=None)
#     Triglycerides = models.IntegerField(null=True, blank=True)
#     Smoker = models.CharField(max_length=3, null=True, blank=True)
#     Blood_type = models.CharField(max_length=3, blank=True, null=True)

#     Dental_checkups = models.BooleanField(default=False)
#     Dental_cleanings = models.BooleanField(default=False)

#     Screen_date = models.DateField(max_length=10,null=True, blank=True,)
    
    
#     def __int__(self):
#         return self.customuser 

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

    # def clean_My_Minor_Symptom_1(self):
    #  My_Minor_Symptom_1 = self.cleaned_data['My_Minor_Symptom_1']

    # # Normalize and decode
    #  My_Minor_Symptom_1 = html.unescape(My_Minor_Symptom_1.lower())

    # # Check for special characters
    #  if '<' in My_Minor_Symptom_1 or '>' in My_Minor_Symptom_1:
    #     raise ValidationError('Invalid health condition. Please avoid using "<" and ">" characters.')

    # # Apply regular expression
    #  if not re.match(r'^[A-Za-z0-9\s-]+$', My_Minor_Symptom_1):
    #     raise ValidationError('Invalid health condition. Please enter only letters, numbers, spaces, and hyphens.')

    #  return My_Minor_Symptom_1

# def clean_My_Minor_Symptom_1(self):
#     My_Minor_Symptom_1 = self.cleaned_data['My_Minor_Symptom_1']

#     # Normalize and decode
#     My_Minor_Symptom_1 = html.unescape(My_Minor_Symptom_1.lower())

#     # Check for common malicious patterns
#     if re.search(r"<[^>]+>", My_Minor_Symptom_1):
#         raise ValidationError("Invalid health condition. Please avoid using HTML tags.")

#     # Check for specific attributes
#     if re.search(r"on[a-z]+=", My_Minor_Symptom_1):
#         raise ValidationError("Invalid health condition. Please avoid using event handlers.")

#     # Apply regular expression
#     if not re.match(r'^[A-Za-z0-9\s-]+$', My_Minor_Symptom_1):
#         raise ValidationError('Invalid health condition. Please enter only letters, numbers, spaces, and hyphens.')

#     return My_Minor_Symptom_1


    def __int__(self):
        return self.customuser



class Myfitness(models.Model):

    customuser = models.OneToOneField(CustomUser, null=False, primary_key=True, on_delete= models.CASCADE)

    moderate_intensity = models.IntegerField(null=True,blank=True)
    vigorous_intensity = models.IntegerField(null=True,blank=True)
    muscle_build = models.IntegerField(null=True,blank=True)
    balance = models.IntegerField(null=True,blank=True)

    def __int__(self):
        return self.customuser  



class Myfoodgroups(models.Model):
    customuser = models.OneToOneField(CustomUser, null=False, primary_key=True, on_delete= models.CASCADE)

    All_veggies = models.IntegerField(null=True,blank=True)
    # Red_Orange_veggies = models.IntegerField(null=True,blank=True)
    Beans_Lentils = models.IntegerField(null=True,blank=True)
    # Other_veggies = models.IntegerField(null=True,blank=True)
    Fruits_Berries = models.IntegerField(null=True,blank=True)
    Protein = models.IntegerField(null=True,blank=True)
    Dairy = models.IntegerField(null=True,blank=True)
   
    Grains = models.IntegerField(null=True,blank=True)

    Allergic1 = models.CharField(max_length=30,  null=True,blank=True)
    Substitute1 = models.CharField(max_length=30,  null=True,blank=True)
    Allergic2 = models.CharField(max_length=30,  null=True,blank=True)
    Substitute2 = models.CharField(max_length=30,  null=True,blank=True)
    Allergic3 = models.CharField(max_length=30,  null=True,blank=True)
    Substitute3 = models.CharField(max_length=30,  null=True,blank=True)
    Allergic4 = models.CharField(max_length=30,  null=True,blank=True)
    Substitute4 = models.CharField(max_length=30,  null=True,blank=True)
    # Herbs_Spices = models.IntegerField(null=True,blank=True)

    def __int__(self):
        return self.customuser

# class Myfoodgroupsver(models.Model):
#     customuser = models.ForeignKey(CustomUser, on_delete= models.CASCADE)
    
#     Green_veggies = models.IntegerField(null=True,blank=True)
#     Red_Orange_veggies = models.IntegerField(null=True,blank=True)
#     Other_veggies = models.IntegerField(null=True,blank=True)
#     Fruits_Berries = models.IntegerField(null=True,blank=True)
#     Protein = models.IntegerField(null=True,blank=True)
#     Dairy = models.IntegerField(null=True,blank=True)
#     Grains = models.IntegerField(null=True,blank=True)
#     Herbs_Spices = models.IntegerField(null=True,blank=True)
    

#     def __int__(self):
#         return self.customuser        

class Myfastfoods(models.Model):
    customuser = models.OneToOneField(CustomUser, null=False, primary_key=True, on_delete= models.CASCADE)
    Bacon = models.CharField(max_length=16,  null=False,blank=False)
    Burgers = models.CharField(max_length=16,  null=False,blank=False)
    Cookies = models.CharField(max_length=16,  null=False,blank=False)
    Cereals = models.CharField(max_length=16,  null=False,blank=False)
    # Canned_foods = models.CharField(max_length=16,  null=False,blank=False, unique=True)
    Frozen_pizza = models.CharField(max_length=16,  null=False,blank=False)
    Ice_cream = models.CharField(max_length=16,  null=False,blank=False)
    Pancakes = models.CharField(max_length=16,  null=False,blank=False)
    Fried_foods = models.CharField(max_length=16,  null=False,blank=False)
    Popcorn = models.CharField(max_length=16,  null=False,blank=False)
    # Margarine = models.CharField(max_length=16, null=False,blank=False, unique=True)
    # Butter = models.CharField(max_length=16,  null=False,blank=False, unique=True)
    Frozen_meals = models.CharField(max_length=16,  null=False,blank=False)
    # Regular_pizza = models.CharField(max_length=16, null=False,blank=False, unique=True)
    French_fries = models.CharField(max_length=16,  null=False,blank=False)
    Potato_chips = models.CharField(max_length=16,  null=False,blank=False)
    Soft_drinks = models.CharField(max_length=16,  null=False,blank=False)
    Milk_shakes = models.CharField(max_length=16,  null=False,blank=False)

    def __int__(self):
        return self.customuser  

# class Myfastfoods_ver(models.Model):
#     customuser = models.ForeignKey(CustomUser, on_delete= models.CASCADE)
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


class Myfoodsuggestions(models.Model):
    customuser = models.OneToOneField(CustomUser, null=False, primary_key=True, on_delete= models.CASCADE)
    Veggie_Salads = models.CharField(max_length=16,  )
    Fruits_Berries = models.CharField(max_length=16,  )
    Dairy = models.CharField(max_length=16,  )
    Veggie_Pasta = models.CharField(max_length=16,  )
    Eggs = models.CharField(max_length=16,  )
    Veggie_Omelettes = models.CharField(max_length=16,  )
    Grains = models.CharField(max_length=16, )
    Herbs_Spices = models.CharField(max_length=16,  )
    Soups =  models.CharField(max_length=16, )
    Herbs_Spices =  models.CharField(max_length=16,  )
    Beans_Legumes =  models.CharField(max_length=16,  )
    Fruit_Smoothies = models.CharField(max_length=16, )
    Veggie_Smoothies = models.CharField(max_length=16, )
    Nuts_Seeds = models.CharField(max_length=16,  )

    def __int__(self):
        return self.customuser  


# class Myallergicfoods(models.Model):
#     customuser = models.OneToOneField(CustomUser, null=False, primary_key=True, on_delete= models.CASCADE)
#     created_at = models.DateTimeField(default=timezone.now,null=True, blank=True )
#     allergicFood1 = models.CharField(max_length=16,  null=True,blank=True)
#     allergicFood2 = models.CharField(max_length=16,  null=True,blank=True)
#     allergicFood3 = models.CharField(max_length=16,  null=True,blank=True)
#     allergicFood4 = models.CharField(max_length=16,  null=True,blank=True)
#     allergicFood5 = models.CharField(max_length=16,  null=True,blank=True)
#     allergicFood6 = models.CharField(max_length=16,  null=True,blank=True)
#     allergicFood7 = models.CharField(max_length=16,  null=True,blank=True)
#     allergicFood8 = models.CharField(max_length=16,  null=True,blank=True)

#     Food_substitute_1 = models.CharField(max_length=16,  null=True,blank=True)
#     Food_substitute_2 = models.CharField(max_length=16,  null=True,blank=True)
#     Food_substitute_3 = models.CharField(max_length=16,  null=True,blank=True)
#     Food_substitute_4 = models.CharField(max_length=16,  null=True,blank=True)
#     Food_substitute_5 = models.CharField(max_length=16,  null=True,blank=True)
   
   
#     def __int__(self):
#         return self.customuser     

# class Myallergicfoods_ver(models.Model):
    
#     customuser = models.ForeignKey(CustomUser, on_delete= models.CASCADE)

#     Regular_Milk = models.BooleanField(default=False)
#     Lactose_free_Milk = models.BooleanField(default=False)
#     Regular_Yogurt = models.BooleanField(default=False)
#     Greek_Yogurt = models.BooleanField(default=False)
#     Peanuts = models.BooleanField(default=False)
#     Walnuts = models.BooleanField(default=False)
#     Pecans = models.BooleanField(default=False)
#     Almonds = models.BooleanField(default=False)
#     Shell_fish = models.BooleanField(default=False)
#     Fish = models.BooleanField(default=False)
#     Soy = models.BooleanField(default=False)
#     Eggs = models.BooleanField(default=False)
#     Sesame = models.BooleanField(default=False)
#     Wheat = models.BooleanField(default=False)
#     Gluten_free_foods = models.BooleanField(default=False)
    
#     Main_Food_1 = models.CharField(max_length=16,  null=True,blank=True)
#     Main_Food_2 = models.CharField(max_length=16,  null=True,blank=True)
#     Main_Food_3 = models.CharField(max_length=16,  null=True,blank=True)
   
#     Food_substitute_1 = models.CharField(max_length=16,  null=True,blank=True, unique=True)
#     Food_substitute_2 = models.CharField(max_length=16,  null=True,blank=True, unique=True)
#     Food_substitute_3 = models.CharField(max_length=16,  null=True,blank=True, unique=True)

#     def __int__(self):
#         return self.customuser      

# class Mytrigfoods(models.Model):
#     customuser = models.OneToOneField(CustomUser, null=False, primary_key=True, on_delete= models.CASCADE)    

#     Trig_Food_1 = models.CharField(max_length=16,  null=True,blank=True, unique=True)
#     Trig_Food_2 = models.CharField(max_length=16,  null=True,blank=True, unique=True)
#     Trig_Food_3 = models.CharField(max_length=16,  null=True,blank=True, unique=True)
#     Trig_Food_4 = models.CharField(max_length=16,  null=True,blank=True, unique=True)

#     Trig_Drink_1 = models.CharField(max_length=16,  null=True,blank=True, unique=True)
#     Trig_Drink_2 = models.CharField(max_length=16,  null=True,blank=True, unique=True)
#     Trig_Drink_3 = models.CharField(max_length=16,  null=True,blank=True, unique=True)

    
#     Foodtrig_substitute_1 = models.CharField(max_length=16,  null=True,blank=True, unique=True)
#     Foodtrig_substitute_2 = models.CharField(max_length=16,  null=True,blank=True, unique=True)
#     Foodtrig_substitute_3 = models.CharField(max_length=16,  null=True,blank=True, unique=True)
#     Foodtrig_substitute_4 = models.CharField(max_length=16,  null=True,blank=True, unique=True)

#     Drink_substitute_1 = models.CharField(max_length=16,  null=True,blank=True, unique=True)
#     Drink_substitute_2 = models.CharField(max_length=16,  null=True,blank=True, unique=True)
#     Drink_substitute_3 = models.CharField(max_length=16,  null=True,blank=True, unique=True)

#     def __int__(self):
#         return self.customuser    

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

class Mytypmeals2(models.Model):

    customuser = models.ForeignKey(CustomUser, on_delete= models.CASCADE)
    
    
    BCuisine = models.CharField(max_length=50, null=True,blank=True)
    B_freq = models.CharField(max_length=16,  null=True, blank=True)
    Breakfast = models.CharField(max_length=50, null=True,blank=True)
    

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


    LCuisine = models.CharField(max_length=50, null=True,blank=True)
    L_freq = models.CharField(max_length=16, null=True, blank=True)
    Lunch = models.CharField(max_length=50, null=True,blank=True)

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

    DCuisine = models.CharField(max_length=50, null=True,blank=True)
    D_freq = models.CharField(max_length=16,  null=True, blank=True)
    Dinner = models.CharField(max_length=50, null=True,blank=True)

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


# class Mytyplunch(models.Model):

#     customuser = models.ForeignKey(CustomUser, on_delete= models.CASCADE)

#     Lunch1 = models.CharField(max_length=50, null=True,blank=True)
#     Cuisine1 = models.CharField(max_length=50, null=True,blank=True)
#     L1_freq = models.CharField(max_length=16, null=True, blank=True)

#     IngredientL11 = models.CharField(max_length=50, null=True,blank=True)    
#     IngredientL12 = models.CharField(max_length=50, null=True,blank=True)
#     IngredientL13 = models.CharField(max_length=50, null=True,blank=True)
#     IngredientL14 = models.CharField(max_length=50, null=True,blank=True)

#     Ingredientdr11 = models.CharField(max_length=50, null=True,blank=True)    
#     Ingredientdr12 = models.CharField(max_length=50, null=True,blank=True)
#     Ingredientdr13 = models.CharField(max_length=50, null=True,blank=True)
#     Ingredientdr14 = models.CharField(max_length=50, null=True,blank=True)

#     Lunch2 = models.CharField(max_length=50, null=True,blank=True)
#     Cuisine2 = models.CharField(max_length=50, null=True,blank=True)
#     L2_freq = models.CharField(max_length=16, null=True, blank=True)

#     IngredientL21 = models.CharField(max_length=50, null=True,blank=True)    
#     IngredientL22 = models.CharField(max_length=50, null=True,blank=True)
#     IngredientL23 = models.CharField(max_length=50, null=True,blank=True)
#     IngredientL24 = models.CharField(max_length=50, null=True,blank=True)

#     Ingredientdr21 = models.CharField(max_length=50, null=True,blank=True)    
#     Ingredientdr22 = models.CharField(max_length=50, null=True,blank=True)
#     Ingredientdr33 = models.CharField(max_length=50, null=True,blank=True)
#     Ingredientdr24 = models.CharField(max_length=50, null=True,blank=True)

class Mytypdinner(models.Model):

    customuser = models.ForeignKey(CustomUser, on_delete= models.CASCADE)

    Dinner1 = models.CharField(max_length=50, null=True,blank=True)
    Cuisine1 = models.CharField(max_length=50, null=True,blank=True)
    D1_freq = models.CharField(max_length=16,  null=True, blank=True)

    IngredientD11 = models.CharField(max_length=50, null=True,blank=True)    
    IngredientD12 = models.CharField(max_length=50, null=True,blank=True)
    IngredientD13 = models.CharField(max_length=50, null=True,blank=True)
    IngredientD14 = models.CharField(max_length=50, null=True,blank=True)

    Ingredientdr11 = models.CharField(max_length=50, null=True,blank=True)    
    Ingredientdr12 = models.CharField(max_length=50, null=True,blank=True)
    Ingredientdr13 = models.CharField(max_length=50, null=True,blank=True)
    Ingredientdr14 = models.CharField(max_length=50, null=True,blank=True)

    Dinner2 = models.CharField(max_length=50, null=True,blank=True)
    Cuisine2 = models.CharField(max_length=50, null=True,blank=True)
    D2_freq = models.CharField(max_length=16,  null=True, blank=True)
    
    IngredientD21 = models.CharField(max_length=50, null=True,blank=True)    
    IngredientD22 = models.CharField(max_length=50, null=True,blank=True)
    IngredientD23 = models.CharField(max_length=50, null=True,blank=True)
    IngredientD24 = models.CharField(max_length=50, null=True,blank=True)

    Ingredientdr21 = models.CharField(max_length=50, null=True,blank=True)    
    Ingredientdr22 = models.CharField(max_length=50, null=True,blank=True)
    Ingredientdr33 = models.CharField(max_length=50, null=True,blank=True)
    Ingredientdr24 = models.CharField(max_length=50, null=True,blank=True)

    def __int__(self):
        return self.customuser


# class Mytypicalmeals_ver(models.Model):

#     customuser = models.ForeignKey(CustomUser, on_delete= models.CASCADE)
#     Breakfast1 = models.CharField(max_length=50, null=True,blank=True)
#     B1_freq = models.CharField(max_length=16,  blank=False)
#     IngredientB11 = models.CharField(max_length=50, null=True,blank=True)    
#     IngredientB12 = models.CharField(max_length=50, null=True,blank=True)
#     IngredientB13 = models.CharField(max_length=50, null=True,blank=True)
#     IngredientB14 = models.CharField(max_length=50, null=True,blank=True)
   

#     Lunch1 = models.CharField(max_length=50, null=True,blank=True)
#     L1_freq = models.CharField(max_length=16,  blank=False)
#     IngredientL11 = models.CharField(max_length=50, null=True,blank=True)    
#     IngredientL12 = models.CharField(max_length=50, null=True,blank=True)
#     IngredientL13 = models.CharField(max_length=50, null=True,blank=True)
#     IngredientL14 = models.CharField(max_length=50, null=True,blank=True)
   

#     Dinner1 = models.CharField(max_length=50, null=True,blank=True)
#     D1_freq = models.CharField(max_length=16,  blank=False)
#     IngredientD11 = models.CharField(max_length=50, null=True,blank=True)    
#     IngredientD12 = models.CharField(max_length=50, null=True,blank=True)
#     IngredientD13 = models.CharField(max_length=50, null=True,blank=True)
#     IngredientD14 = models.CharField(max_length=50, null=True,blank=True)
    

#     def __int__(self):
#         return self.customuser

# class Mybreakfast(models.Model):
#     Cuisine1 = models.CharField(max_length=20, null=True,blank=True)
#     Breakfast1 = models.CharField(max_length=20, null=True,blank=True)
#     B1_freq = models.CharField(max_length=18,  null=True,blank=True)
#     breakfast_source1 = models.CharField(max_length=12, null=True,blank=True)

#     Cuisine2 = models.CharField(max_length=20, null=True,blank=True)
#     Breakfast2 = models.CharField(max_length=20, null=True,blank=True)
#     B2_freq = models.CharField(max_length=18,  null=True,blank=True)
#     breakfast_source2 = models.CharField(max_length=12, null=True,blank=True)

#     Cuisine3 = models.CharField(max_length=20, null=True,blank=True)
#     Breakfast3 = models.CharField(max_length=20, null=True,blank=True)
#     B3_freq = models.CharField(max_length=18,  null=True,blank=True)
#     breakfast_source3 = models.CharField(max_length=12, null=True,blank=True)

#     Cuisine4 = models.CharField(max_length=20, null=True,blank=True)
#     Breakfast4 = models.CharField(max_length=20, null=True,blank=True)
#     B4_freq = models.CharField(max_length=18,  null=True,blank=True)
#     breakfast_source4 = models.CharField(max_length=12, null=True,blank=True)

# class Mylunch(models.Model):
#     Cuisine1 = models.CharField(max_length=20, null=True,blank=True)
#     Lunch1 = models.CharField(max_length=20, null=True,blank=True)
#     L1_freq = models.CharField(max_length=18,  null=True,blank=True)
#     lunch_source1 = models.CharField(max_length=12, null=True,blank=True)

#     Cuisine2 = models.CharField(max_length=20, null=True,blank=True)
#     Lunch2 = models.CharField(max_length=20, null=True,blank=True)
#     L2_freq = models.CharField(max_length=18,  null=True,blank=True)
#     lunch_source2 = models.CharField(max_length=12, null=True,blank=True)

#     Cuisine3 = models.CharField(max_length=20, null=True,blank=True)
#     Lunch3 = models.CharField(max_length=20, null=True,blank=True)
#     L3_freq = models.CharField(max_length=18,  null=True,blank=True)
#     lunch_source3 = models.CharField(max_length=12, null=True,blank=True)

#     Cuisine4 = models.CharField(max_length=20, null=True,blank=True)
#     Lunch4 = models.CharField(max_length=20, null=True,blank=True)
#     L4_freq = models.CharField(max_length=18,  null=True,blank=True)
#     lunch_source4 = models.CharField(max_length=12, null=True,blank=True)

# class Mydinner(models.Model):
#     Cuisine1 = models.CharField(max_length=20, null=True,blank=True)
#     Dinner1 = models.CharField(max_length=20, null=True,blank=True)
#     D1_freq = models.CharField(max_length=18,  null=True,blank=True)
#     dinner_source1 = models.CharField(max_length=12, null=True,blank=True)

#     Cuisine2 = models.CharField(max_length=20, null=True,blank=True)
#     Dinner2 = models.CharField(max_length=20, null=True,blank=True)
#     D2_freq = models.CharField(max_length=18,  null=True,blank=True)
#     dinner_source2 = models.CharField(max_length=12, null=True,blank=True)

#     Cuisine3 = models.CharField(max_length=20, null=True,blank=True)
#     Dinner3 = models.CharField(max_length=20, null=True,blank=True)
#     D3_freq = models.CharField(max_length=18,  null=True,blank=True)
#     dinner_source3 = models.CharField(max_length=12, null=True,blank=True)

#     Cuisine4 = models.CharField(max_length=20, null=True,blank=True)
#     Dinner4 = models.CharField(max_length=20, null=True,blank=True)
#     D4_freq = models.CharField(max_length=18,  null=True,blank=True)
#     dinner_source4 = models.CharField(max_length=12, null=True,blank=True)

# class Mycuisinemeals(models.Model):
#     customuser = models.OneToOneField(CustomUser, null=False, primary_key=True, on_delete= models.CASCADE)
#     US_Generic = models.CharField(max_length=16,   db_index=False)
#     Chinese = models.CharField(max_length=16,  db_index=False)
#     Mexican = models.CharField(max_length=16,  db_index=False)
#     Thai = models.CharField(max_length=16,   db_index=False)
#     Indian = models.CharField(max_length=16,   db_index=False)
#     Italian = models.CharField(max_length=16,    db_index=False)
#     Mediterranean = models.CharField(max_length=16,    db_index=False)
#     Vietnamese = models.CharField(max_length=16,    db_index=False)
#     Japanese = models.CharField(max_length=16,   db_index=False)

#     Scrambled_eggs = models.BooleanField(default=False,  db_index=False)
#     Pancakes = models.BooleanField(default=False,  db_index=False)
#     Boiled_eggs = models.BooleanField(default=False,  db_index=False)
#     Oatmeal = models.BooleanField(default=False,  db_index=False)
#     Fruit_juices = models.BooleanField(default=False,  db_index=False)
#     Non_beef_burgers = models.BooleanField(default=False,  db_index=False)
#     Salads = models.BooleanField(default=False, db_index=False)
#     Omelettes = models.BooleanField(default=False,  db_index=False)
#     Bagels = models.BooleanField(default=False, unique=True, db_index=False)
#     Egg_salad_sandwich = models.BooleanField(default=False,  db_index=False)
#     Veggie_sandwich = models.BooleanField(default=False,  db_index=False)

#     Stirfry_noodles = models.BooleanField(default=False,  db_index=False)
#     Fried_Rice = models.BooleanField(default=False,  db_index=False)
#     Sweet_sour_based = models.BooleanField(default=False,  db_index=False)
#     Hot_Sour_Soup = models.BooleanField(default=False,  db_index=False)
#     Egg_Drop_Soup = models.BooleanField(default=False,  db_index=False)
#     General_Tsos_based = models.BooleanField(default=False,  db_index=False)
#     Mogolian_based = models.BooleanField(default=False,  db_index=False)
#     Orange_sauce_based = models.BooleanField(default=False,  db_index=False)
#     Chinese_dumplings = models.BooleanField(default=False,  db_index=False)
#     Garlic_eggplant_sauce = models.BooleanField(default=False,  db_index=False)

#     Tacos = models.BooleanField(default=False,  db_index=False)
#     Fajitas = models.BooleanField(default=False,  db_index=False)
#     Migas = models.BooleanField(default=False,  db_index=False)
#     Quesadillas = models.BooleanField(default=False,  db_index=False)
#     Tortilla_soup = models.BooleanField(default=False,  db_index=False)
#     Enchiladas = models.BooleanField(default=False,  db_index=False)
#     Mexican_rice = models.BooleanField(default=False,  db_index=False)
#     Burritos = models.BooleanField(default=False,  db_index=False)
#     Burrito_bowl = models.BooleanField(default=False,  db_index=False)
#     Mexican_Soup = models.BooleanField(default=False, db_index=False)

#     Pad_thai = models.BooleanField(default=False,  db_index=False)
#     Pumpkin_soup = models.BooleanField(default=False,  db_index=False)
#     Thai_red_curry = models.BooleanField(default=False,  db_index=False)
#     Tom_Kha_soup = models.BooleanField(default=False,  db_index=False)
#     Thai_fried_rice = models.BooleanField(default=False,  db_index=False)
#     Spring_rolls = models.BooleanField(default=False, db_index=False)
#     Tom_Yum_soup = models.BooleanField(default=False, db_index=False)
#     Pineapple_fried_rice = models.BooleanField(default=False,  db_index=False)

#     Chick_peas_curry = models.BooleanField(default=False,  db_index=False)
#     Sambar = models.BooleanField(default=False,  db_index=False)
#     Aloo_gobi = models.BooleanField(default=False,  db_index=False)
#     Indian_Tomato_soup = models.BooleanField(default=False,  db_index=False)
#     Onion_Mushroom_curry = models.BooleanField(default=False,  db_index=False)
#     Tamarind_rice = models.BooleanField(default=False,  db_index=False)
#     Kidney_beans_curry = models.BooleanField(default=False,  db_index=False)
#     Tomato_Rasam_curry = models.BooleanField(default=False,  db_index=False)
#     Okra_curry = models.BooleanField(default=False,  db_index=False)
#     Lemon_rice = models.BooleanField(default=False,  db_index=False)
#     Pepper_Garlic_Soup = models.BooleanField(default=False,  db_index=False)
#     Pulao = models.BooleanField(default=False,  db_index=False)

#     Eggplant_Parmesan = models.BooleanField(default=False, db_index=False)
#     Pasta = models.BooleanField(default=False,  db_index=False)
#     Alfredo_noodles = models.BooleanField(default=False,  db_index=False)
#     Tortellini_soup = models.BooleanField(default=False,  db_index=False)
#     Minestrone_soup = models.BooleanField(default=False,  db_index=False)
#     Brushetta = models.BooleanField(default=False, db_index=False)
#     Lasagna = models.BooleanField(default=False, db_index=False)
#     Eggplant_sandwich = models.BooleanField(default=False, db_index=False)
    
    
    # Pho_soup = models.BooleanField(default=False, unique=True)
    # Vietnamese_crepes = models.BooleanField(default=False, unique=True)
    # Avocado_smoothie = models.BooleanField(default=False, unique=True)
    # Vietnamese_curry = models.BooleanField(default=False, unique=True)
    # Banh_Mi = models.BooleanField(default=False, unique=True)
    # Jackfruit_smoothie = models.BooleanField(default=False, unique=True)
    # Vietnamese_stirfry = models.BooleanField(default=False, unique=True)
    # Tofu_tomato_sauce = models.BooleanField(default=False, unique=True)

    # Poke_Bowl = models.BooleanField(default=False, unique=True)
    # Miso_soup = models.BooleanField(default=False, unique=True)
    # Eggplant_Donbury = models.BooleanField(default=False, unique=True)
    # Ramen_Noodles = models.BooleanField(default=False, unique=True)
    # Japanese_Curry = models.BooleanField(default=False, unique=True)
    # Grilled_Rice_balls = models.BooleanField(default=False, unique=True)

    # Brushetta_Tartines = models.BooleanField(default=False, unique=True)
    # Quinoa_salad = models.BooleanField(default=False, unique=True)
    # Lentil_Soup = models.BooleanField(default=False, unique=True)
    # Stuffed_Grape_leaves = models.BooleanField(default=False, unique=True)
    # Chickpea_Burger = models.BooleanField(default=False, unique=True)
    # Caponata = models.BooleanField(default=False, unique=True)
    # Falafel = models.BooleanField(default=False, unique=True)
    # Spanish_potato_omelette = models.BooleanField(default=False, unique=True)

    
    # def __int__(self):
    #     return self.customuser


class Myeatoutmeals(models.Model):

    customuser = models.OneToOneField(CustomUser, null=False, primary_key=True, on_delete= models.CASCADE)
    Restaurant1 = models.CharField(max_length=50, null=True,blank=True, unique=True)
    Breakfast1 = models.CharField(max_length=50, null=True,blank=True, unique=True)
    IngredientB11 = models.CharField(max_length=50, null=True,blank=True, unique=True)    
    IngredientB12 = models.CharField(max_length=50, null=True,blank=True, unique=True)
    IngredientB13 = models.CharField(max_length=50, null=True,blank=True, unique=True)
    IngredientB14 = models.CharField(max_length=50, null=True,blank=True, unique=True)
    IngredientB15 = models.CharField(max_length=50, null=True,blank=True, unique=True)
    IngredientB16 = models.CharField(max_length=50, null=True,blank=True, unique=True)

    Restaurant2 = models.CharField(max_length=50, null=True,blank=True, unique=True)
    Breakfast2 = models.CharField(max_length=50, null=True,blank=True, unique=True)

    IngredientB21 = models.CharField(max_length=50, null=True,blank=True, unique=True)    
    IngredientB22 = models.CharField(max_length=50, null=True,blank=True, unique=True)
    IngredientB23 = models.CharField(max_length=50, null=True,blank=True, unique=True)
    IngredientB24 = models.CharField(max_length=50, null=True,blank=True, unique=True)
    IngredientB25 = models.CharField(max_length=50, null=True,blank=True, unique=True)
    IngredientB26 = models.CharField(max_length=50, null=True,blank=True, unique=True)

    Restaurant3 = models.CharField(max_length=50, null=True,blank=True, unique=True)
    Lunch1 = models.CharField(max_length=50, null=True,blank=True, unique=True)
    IngredientL11 = models.CharField(max_length=50, null=True,blank=True, unique=True)    
    IngredientL12 = models.CharField(max_length=50, null=True,blank=True, unique=True)
    IngredientL13 = models.CharField(max_length=50, null=True,blank=True, unique=True)
    IngredientL14 = models.CharField(max_length=50, null=True,blank=True, unique=True)
    IngredientL15 = models.CharField(max_length=50, null=True,blank=True, unique=True)
    IngredientL16 = models.CharField(max_length=50, null=True,blank=True, unique=True)

    Restaurant4 = models.CharField(max_length=50, null=True,blank=True, unique=True)
    Lunch2 = models.CharField(max_length=50, null=True,blank=True, unique=True)
    IngredientL21 = models.CharField(max_length=50, null=True,blank=True, unique=True)    
    IngredientL22 = models.CharField(max_length=50, null=True,blank=True, unique=True)
    IngredientL23 = models.CharField(max_length=50, null=True,blank=True, unique=True)
    IngredientL24 = models.CharField(max_length=50, null=True,blank=True, unique=True)
    IngredientL25 = models.CharField(max_length=50, null=True,blank=True, unique=True)
    IngredientL26 = models.CharField(max_length=50, null=True,blank=True, unique=True)

    Restaurant5 = models.CharField(max_length=50, null=True,blank=True, unique=True)
    Dinner1 = models.CharField(max_length=50, null=True,blank=True, unique=True)
    IngredientD11 = models.CharField(max_length=50, null=True,blank=True, unique=True)    
    IngredientD12 = models.CharField(max_length=50, null=True,blank=True, unique=True)
    IngredientD13 = models.CharField(max_length=50, null=True,blank=True, unique=True)
    IngredientD14 = models.CharField(max_length=50, null=True,blank=True, unique=True)
    IngredientD15 = models.CharField(max_length=50, null=True,blank=True, unique=True)
    IngredientD16 = models.CharField(max_length=50, null=True,blank=True, unique=True)

    Restaurant6 = models.CharField(max_length=50, null=True,blank=True, unique=True)
    Dinner2 = models.CharField(max_length=50, null=True,blank=True, unique=True)
    IngredientD21 = models.CharField(max_length=50, null=True,blank=True, unique=True)    
    IngredientD22 = models.CharField(max_length=50, null=True,blank=True, unique=True)
    IngredientD23 = models.CharField(max_length=50, null=True,blank=True, unique=True)
    IngredientD24 = models.CharField(max_length=50, null=True,blank=True, unique=True)
    IngredientD25 = models.CharField(max_length=50, null=True,blank=True, unique=True)
    IngredientD26 = models.CharField(max_length=50, null=True,blank=True, unique=True)

    def __int__(self):
        return self.customuser        

class Myexpenses(models.Model):

        customuser = models.OneToOneField(CustomUser, null=False, primary_key=True, on_delete= models.CASCADE)
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

class Myexpenses_ver(models.Model):

        customuser = models.ForeignKey(CustomUser, on_delete= models.CASCADE)
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


class Myhabits(models.Model):   
        customuser = models.OneToOneField(CustomUser, null=False, primary_key=True, on_delete= models.CASCADE)
        Morning_stretches = models.BooleanField(default=False)
        Healthy_breakfast = models.BooleanField(default=False)
        Water = models.BooleanField(default=False)
        Healthy_lunch = models.BooleanField(default=False)
        Daily_fitness = models.BooleanField(default=False)
        Reduce_processed = models.BooleanField(default=False)
        Prepare_simple_meals = models.BooleanField(default=False)
        Daily_savings = models.BooleanField(default=False)
        Night_stretches = models.BooleanField(default=False)
        Kitchen_clean = models.BooleanField(default=False)
        # No_late_nights = models.BooleanField(default=False)
        # Night_floss = models.BooleanField(default=False)
        
        Shop_list = models.BooleanField(default=False)
        Shopping = models.BooleanField(default=False)
        Clean_car = models.BooleanField(default=False)
        Clean_house = models.BooleanField(default=False)
        Potluck_cook = models.BooleanField(default=False)
        Laundry = models.BooleanField(default=False)
        Weekly_fitness = models.BooleanField(default=False)
        Book_podcast = models.BooleanField(default=False)
        Weekly_savings = models.BooleanField(default=False)
        Mindful_yoga = models.BooleanField(default=False)
        Weekly_suggestions = models.BooleanField(default=False)
        Weekly_log = models.BooleanField(default=False)
        Weekly_feedback = models.BooleanField(default=False)

        Daily_habit_1 = models.CharField(max_length=30,  null=True,blank=True, unique=True)
        Daily_habit_2 = models.CharField(max_length=30,  null=True,blank=True, unique=True)
        Weekly_habit_1 = models.CharField(max_length=30,  null=True,blank=True, unique=True)
        Weekly_habit_2 = models.CharField(max_length=30,  null=True,blank=True, unique=True)

        def __int__(self):
          return self.customuser



# class Myschedule(models.Model):

#     customuser = models.OneToOneField(CustomUser, null=False, primary_key=True, on_delete= models.CASCADE)
#     Meal_date1 = models.DateField(max_length=10,null=True, blank=True,)       
#     Meal_date2 = models.DateField(max_length=10,null=True, blank=True,)
#     Meal_date3 = models.DateField(max_length=10,null=True, blank=True,)
#     Meal_date4 = models.DateField(max_length=10,null=True, blank=True,)
#     Meal_date5 = models.DateField(max_length=10,null=True, blank=True,)
#     Meal_date6 = models.DateField(max_length=10,null=True, blank=True,)
#     Meal_date7 = models.DateField(max_length=10,null=True, blank=True,)

#     Fit_date1 = models.DateField(max_length=10,null=True, blank=True,)
#     Fit_date2 = models.DateField(max_length=10,null=True, blank=True,)
#     Fit_date3 = models.DateField(max_length=10,null=True, blank=True,)
#     Fit_date4 = models.DateField(max_length=10,null=True, blank=True,)
#     Fit_date5 = models.DateField(max_length=10,null=True, blank=True,)
#     Fit_date6 = models.DateField(max_length=10,null=True, blank=True,)
#     Fit_date7 = models.DateField(max_length=10,null=True, blank=True,)

# class fruitberries(models.Model):

#     customuser = models.OneToOneField(CustomUser, null=False, primary_key=True, on_delete= models.CASCADE)


#     Apples = models.CharField(max_length=10, null=True, blank=True, unique=True) 
#     Include_Apples = models.BooleanField(default=True)  

#     Apricot = models.CharField(max_length=10,null=True, blank=True, unique=True) 
#     Include_Apricots = models.BooleanField(default=True) 

#     Banana = models.CharField(max_length=10, null=True, blank=True,unique=True) 
#     Include_Bananas = models.BooleanField(default=True) 

#     Cantaloupe = models.CharField(max_length=10, null=True, blank=True,unique=True) 
#     Include_Cantaloupe = models.BooleanField(default=True) 

#     Dates = models.CharField(max_length=10, null=True, blank=True,unique=True) 
#     Include_Dates = models.BooleanField(default=True) 

#     Grapes = models.CharField(max_length=10, null=True, blank=True,unique=True) 
#     Include_Grapes = models.BooleanField(default=True) 

#     Guava = models.CharField(max_length=10, null=True, blank=True,unique=True) 
#     Include_Guava = models.BooleanField(default=True) 

#     Kiwi = models.CharField(max_length=10, null=True, blank=True,unique=True) 
#     Include_Kiwi = models.BooleanField(default=True) 

#     Mango = models.CharField(max_length=10, null=True, blank=True,unique=True) 
#     Include_Mango = models.BooleanField(default=True)         

#     Papaya = models.CharField(max_length=10, null=True, blank=True,unique=True) 
#     Include_Papaya = models.BooleanField(default=True) 

#     Pineapple = models.CharField(max_length=10, null=True, blank=True,unique=True) 
#     Include_Pineapple = models.BooleanField(default=True) 

#     Plum = models.CharField(max_length=10, null=True, blank=True,unique=True) 
#     Include_Plum = models.BooleanField(default=True) 

#     Peach = models.CharField(max_length=10, null=True, blank=True,unique=True) 
#     Include_Peach = models.BooleanField(default=True) 

#     Blueberries = models.CharField(max_length=10, null=True, blank=True,unique=True) 
#     Include_Blueberries = models.BooleanField(default=True)

#     Blackberries = models.CharField(max_length=10, null=True, blank=True,unique=True) 
#     Include_Blackberries = models.BooleanField(default=True) 

#     Cranberries = models.CharField(max_length=10, null=True, blank=True,unique=True) 
#     Include_Cranberries = models.BooleanField(default=True) 

#     Cherries = models.CharField(max_length=10, null=True, blank=True,unique=True) 
#     Include_Cherries = models.BooleanField(default=True) 

#     Strawberries = models.CharField(max_length=10, null=True, blank=True,unique=True) 
#     Include_Strawberries = models.BooleanField(default=True) 

class Supplements(models.Model):
          
    customuser = models.ForeignKey(CustomUser, on_delete= models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now,null=True, blank=True )
    Supplement_1 = models.CharField(max_length=100, null=True, blank=True,unique=True)
    Supplement_2 = models.CharField(max_length=100, null=True, blank=True,unique=True)
    Supplement_3 = models.CharField(max_length=100, null=True, blank=True,unique=True)
    Supplement_4 = models.CharField(max_length=100, null=True, blank=True,unique=True)
    Supplement_5 = models.CharField(max_length=100, null=True, blank=True,unique=True)
    Supplement_6 = models.CharField(max_length=100, null=True, blank=True,unique=True)
    Supplement_7 = models.CharField(max_length=100, null=True, blank=True,unique=True)
    Supplement_8 = models.CharField(max_length=100, null=True, blank=True,unique=True)
    Supplement_9 = models.CharField(max_length=100, null=True, blank=True,unique=True)
    Supplement_10 = models.CharField(max_length=100, null=True, blank=True,unique=True)

# class Supplements_ver(models.Model):
          
#     customuser = models.ForeignKey(CustomUser, on_delete= models.CASCADE)
#     created_at = models.DateTimeField(default=timezone.now,null=True, blank=True )
#     Supplement_1 = models.CharField(max_length=100, null=True, blank=True)
#     Supplement_2 = models.CharField(max_length=100, null=True, blank=True)
#     Supplement_3 = models.CharField(max_length=100, null=True, blank=True)
#     Supplement_4 = models.CharField(max_length=100, null=True, blank=True)
#     Supplement_5 = models.CharField(max_length=100, null=True, blank=True)
#     Supplement_6 = models.CharField(max_length=100, null=True, blank=True)
#     Supplement_7 = models.CharField(max_length=100, null=True, blank=True)
#     Supplement_8 = models.CharField(max_length=100, null=True, blank=True)
#     Supplement_9 = models.CharField(max_length=100, null=True, blank=True)
#     Supplement_10 = models.CharField(max_length=100, null=True, blank=True)    
        
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