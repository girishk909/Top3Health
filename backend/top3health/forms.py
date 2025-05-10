from django import forms
from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
# from .models import Goals
# from .models import Goals_ver
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.admin.widgets import AdminTimeWidget
from django.forms.fields import DateField

from .models import Study
# from .models import MyProfile
# from .models import MyProfile_ver
from .models import Myhealthscreening
# from .models import Myhealthscreening_ver
from .models import Healthsym
# from .models import Minorsym_ver
# from .models import Majorsym
# from .models import Majorsym_ver
from .models import Myfitness
# from .models import Myfitness_ver
from .models import Myfoodgroups
# from .models import Myfoodgroupsver
# from .models import Myfastfoods
# from .models import Myfastfoods_ver
# from .models import Myallergicfoods
# from .models import Mytrigfoods
# from .models import Mytypicalmeals
# from .models import Mytypicalmeals_ver
# from .models import Myeatoutmeals
# from .models import Myschedule
# from .models import fruitberries
from .models import Supplements
# from .models import Supplements_ver
# from .models import Mycuisinemeals
# from .models import Myallergicfoods
# rfom .models import Myallergicfoods_ver
from .models import Mytypmeals1
# from .models import Mytypmeals2
# # from .models import Mybreakfast
# from .models import Mylunch
# from .models import Mydinner
from .models import Mydailylog
# from .models import CustomRole
from .models import Beginpage
from .models import Dietician_note


from .models import Myfoodsuggestions
from .models import Myexpenses
from .models import Mymonthlyexpenses
# from .models import Myexpenses_ver
from .models import Myhabits
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field
from django.utils.safestring import mark_safe


from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.admin.widgets import FilteredSelectMultiple    
from django.contrib.auth.models import Group



User = get_user_model()


# Create ModelForm based on the Group model.
class GroupAdminForm(forms.ModelForm):
    class Meta:
        model = Group
        exclude = []

    # Add the users field.
    users = forms.ModelMultipleChoiceField(
         queryset=User.objects.all(), 
         required=False,
         # Use the pretty 'filter_horizontal widget'.
         widget=FilteredSelectMultiple('users', False)
    )

    def __init__(self, *args, **kwargs):
        # Do the normal form initialisation.
        super(GroupAdminForm, self).__init__(*args, **kwargs)
        # If it is an existing group (saved objects have a pk).
        if self.instance.pk:
            # Populate the users field with the current Group users.
            self.fields['users'].initial = self.instance.user_set.all()

    def save_m2m(self):
        # Add the users to the Group.
        self.instance.user_set.set(self.cleaned_data['users'])

    def save(self, *args, **kwargs):
        # Default save
        instance = super(GroupAdminForm, self).save()
        # Save many-to-many data
        self.save_m2m()
        return instance

class CustomUserCreationForm(UserCreationForm):
  class Meta:
    model = CustomUser
    fields = UserCreationForm.Meta.fields + ('first_name',  'last_name', 'middle_initial', 'email', 'Height_ft', 'Height_in','Weight_in_pounds', 'Gender','address_1', 'address_2', 'zipcode', 'city', 'state', 'phone_number', 'dob',)
    #fields = '__all__'
    # exclude = ['date_joined']
    #exclude = ['password1']
   # exclude = ['password2']

    # widgets = {
    #     'dob': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),

    # }

    # password1 = forms.CharField(label='password', widget=forms.PasswordInput)  
    # password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)  
  
    # def username_clean(self):  
    #     username = self.cleaned_data['username'].lower()  
    #     new = User.objects.filter(username = username)  
    #     if new.count():  
    #         raise ValidationError("User Already Exists")  
    #     return username  
  
    # def email_clean(self):  
    #     email = self.cleaned_data['email'].lower()  
    #     new = User.objects.filter(email=email)  
    #     if new.count():  
    #         raise ValidationError(" Email Already Exists")  
    #     return email  
  
    # def clean_password2(self):  
    #     password1 = self.cleaned_data['password1']  
    #     password2 = self.cleaned_data['password2']  
  
    #     if password1 and password2 and password1 != password2:  
    #         raise ValidationError("Password don't match")  
    #     return password2    

# class CustomerForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)

#     def __init__(self, *args, **kwargs):
#          super(CustomUserCreationForm, self).__init__(*args, **kwargs)  
#          dob=forms.DateField(widget = forms.SelectDateWidget())
#          dob = DateField(widget=AdminDateWidget)
#          self.fields['dob'].widget.attrs['style'] = 'font-size:18px; margin-bottom:70px;'
#          self.fields['dob'].widget.attrs.update({'class': 'form-control',})
#          self.fields['username'].widget.attrs.update({'class': 'form-control2',})
#          self.fields['username'].widget.attrs['style'] = 'margin-left:0px; font-size:15px; padding-top:-10px;'
  
         
#          self.fields['first_name'].help_text = 'Some text'

class CustomUserChangeForm(UserChangeForm):
  class Meta:
    model = CustomUser
    fields = UserChangeForm.Meta.fields

# class StudyForm(forms.ModelForm):
#     class Meta:
#         model = Study
#         fields = '__all__'

class StaffRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        # fields = ('first_name', 'last_name', 'phone_number', 'role',)
        exclude = ('groups', 'user_permissions', 'is_active','Height_ft', 'Height_in', 'Weight_in_pounds', 'Gender', 'address_1', 'address_2', 'city',
                    'state', 'zipcode','is_staff', 'password', 'last_login', )
        field_order = [ 'username','first_name', 'last_name', 'Middle_initial', 'Email','phone_number', 'role',   
                       'mode', 'study_type', ]            
        

class DieticiannoteForm(forms.ModelForm):                
 class Meta:
    model = Dietician_note
    fields =  ['created_at','note1','note2','note3','note4','note5','note6','note7','note8','note9','note10']

class StudyForm(forms.ModelForm):
    class Meta:
        model = Study
        fields = ['study_topic']    

# class CustomRoleForm(forms.ModelForm):
#     class Meta:
#         model = CustomRole
#         fields = ['role_type']            

class MydailylogForm(forms.ModelForm):
    class Meta:
        model = Mydailylog


        fields = ['Breakfast_name', 'Lunch_name', 'Dinner_name', 'Breakfast_description', 'Lunch_description', 'Dinner_description','veggies','beans_lentils', 'fruits_berries', 'dairy', 'grains', 'protein', 'moderate_intensity_type','moderate_intensity', 'vigorous_intensity_type','vigorous_intensity', 
        'muscle_build_type','muscle_build', 'balance_type','balance', 'Stretches', 'Stretch_check', 'Reduce_processed', 'Reduce_processed_check', 'Prepare_meals', 'Prepare_meals_check', 
        'Wake_time', 'Wake_time_check', 'food_cost_savings', 'food_savings_check', 'Clear_kitchen', 'Clear_kitchen_check', 'Brush_Floss', 'Brush_Floss_check', 
        'Groceries_shop', 'Groceries_shop_check', 'daily_mindfulness', 'daily_mindfulness_check', 'food_suggestions', 'food_suggestions_check', 'reduce_alcohol',
        'reduce_alcohol_check', 'reduce_smoking', 'reduce_smoking_check',  'custom_habit_1', 'custom_habit_1_check', 'custom_habit_2', 'custom_habit_2_check',
        'custom_habit_3', 'custom_habit_3_check', 'daily_eatout_cost', 'daily_misc_cost', 'daily_grocery_cost', 'date', ]         


class BeginpageForm(forms.ModelForm):

    class Meta():
        model = Beginpage
        fields = ['created_at', 'begin_date', 'daily_log_time', 'weekly_log_time', 'weekly_suggestion_time']

        widgets = {
            'begin_date': forms.SelectDateWidget(
                 empty_label=("Choose Year", "Choose Month", "Choose Day"),
            ),
            'time1': forms.TimeInput(format='%H:%M'),
        }    

class MyexpensesForm(forms.ModelForm):
    class Meta:
      model = Myexpenses
      fields = ['family_eatout_count', 'weekly_eatout_cost', 'family_grocery_count', 'weekly_grocery_cost', 'Misc_expense_member', 'Misc_expenses', 
    'family_premium_count', 'insurance_premium', 'members_for_office_visit', 'office_visit_cost', 'members_for_prescriptions', 'prescription_cost', 
    'members_for_oop', 'oop_cost', 'members_for_gym', 'gym_cost']
    def __int__(self, *args, **kwargs):
        super(MyexpensesForm, self).__int__(*args, **kwargs)

class MymonthlyexpensesForm(forms.ModelForm):
     class Meta:
      model = Mymonthlyexpenses   
      fields = [
        'family_premium_count', 'insurance_premium', 'members_for_office_visit', 'office_visit_cost',
        'members_for_prescriptions', 'prescription_cost', 'members_for_oop', 'oop_cost', 'members_for_gym', 'gym_cost'
      ]  

# class MyexpensesverForm(forms.ModelForm):
#     class Meta:
#       model = Myexpenses_ver
#       fields = ['family_eatout_count', 'weekly_eatout_cost', 'family_grocery_count', 'weekly_grocery_cost', 'Misc_expense_member', 'Misc_expenses', 
#     'family_premium_count', 'insurance_premium', 'members_for_office_visit', 'office_visit_cost', 'members_for_prescriptions', 'prescription_cost', 
#     'members_for_oop', 'oop_cost', 'members_for_gym', 'gym_cost']
#     def __int__(self, *args, **kwargs):
#         super(MyexpensesverForm, self).__int__(*args, **kwargs)


class MyhabitsForm(forms.ModelForm):    
     class Meta:
      model = Myhabits
      fields = ['created_at','Stretches', 'Reduce_processed', 'Prepare_meals', 'food_cost_savings', 'daily_mindfulness', 'food_suggestions', 'reduce_alcohol', 'reduce_smoking',
      'Clear_kitchen',  'Groceries_shop',
      'Wake_time', 'Brush_Floss']
      def __int__(self, *args, **kwargs):
        super(MyhabitsForm, self).__int__(*args, **kwargs)     

# class ProfileForm(forms.ModelForm):
#   class Meta:
#     model = MyProfile
#     fields = ['Height_ft', 'Height_in','Weight_in_pounds', 'Gender', 'Calories_intake', 'Calories_burned', 'Protein_intake', 'Carbs_intake', 'Water_intake', 'Stress_level', 'Sleep_quality', 'Race', 'Ethnicity']  
#     Height_ft = forms.CharField(help_text=('Please enter a single digit upto 8.'))
  
  
#   def __int__(self, *args, **kwargs):
#         super(ProfileForm, self).__int__(*args, **kwargs)
        
# class ProfileverForm(forms.ModelForm):
#   class Meta:
#     model = MyProfile_ver
#     fields = ['Height_ft', 'Height_in', 'Weight_in_pounds', 'Gender', 'Calories_intake', 'Calories_burned', 'Protein_intake', 'Carbs_intake', 'Water_intake', 'Stress_level', 'Sleep_quality', 'Race', 'Ethnicity']  
#   def __int__(self, *args, **kwargs):
#         super(ProfileverForm, self).__int__(*args, **kwargs)


class MyhealthscreeningForm(forms.ModelForm):
  class Meta:
    model = Myhealthscreening
    fields = ['Blood_glucose', 'A1C', 'BP_systolic', 'BP_diastolic', 'Total_Cholesterol', 'HDL', 'LDL', 'Triglycerides', 'Smoker', 'Blood_type','dental_date', 'vision_date','Screen_date']  
  def __int__(self, *args, **kwargs):
        super(MyhealthscreeningForm, self).__int__(*args, **kwargs)
  
# class MyhealthscreeningverForm(forms.ModelForm):
#   class Meta:
#     model = Myhealthscreening_ver
#     fields = ['Blood_glucose', 'A1C', 'BP_systolic', 'BP_diastolic', 'Total_Cholesterol', 'HDL', 'LDL', 'Triglycerides', 'Smoker', 'Blood_type','Dental_checkups', 'Dental_cleanings', 'Screen_date']  
#   def __int__(self, *args, **kwargs):
#         super(MyhealthscreeningverForm, self).__int__(*args, **kwargs)

class HealthsymForm(forms.ModelForm):

  class Meta:
    model = Healthsym
    fields = ['created_at','Minor1','Minor2', 'Minor3', 'Minor4', 'Minor5', 'Major1','Major2', 'Major3','Major4', 'Major5', 'physical_health', 'mental_health', 'social_relations', 'access_health_food',
    ]
  def __int__(self, *args, **kwargs):
        super(HealthsymForm, self).__int__(*args, **kwargs)

# class MinorsymverForm(forms.ModelForm):

#   class Meta:
#     model = Minorsym_ver
#     fields = ['Fatigue', 'Lack_of_focus', 'Insomnia', 'Migraine',  'Body_Pain',  'Constipation', 'Minor_skin_issues', 'Frequent_sickness','ADD_ADHD',  'Low_motivation', 'My_Minor_Symptom_1', 'My_Minor_Symptom_2',
#     ]
#   def __int__(self, *args, **kwargs):
#         super(MinorsymverForm, self).__int__(*args, **kwargs)  


# class MajorsymForm(forms.ModelForm):

#   class Meta:
#     model = Majorsym
#     fields = ['created_at','Major1','Major2', 'Major3','My_Major_Symptom_1', 'My_Major_Symptom_2',
#     ]
#   def __int__(self, *args, **kwargs):
#         super(MajorsymForm, self).__int__(*args, **kwargs)

# class MajorsymverForm(forms.ModelForm):

  # class Meta:
  #   model = Majorsym_ver
  #   fields = ['Cardiovascular_CVD', 'Obesity', 'Pre_Diabetes','Diabetes', 'Hypothyroid',  'Hyperthyroid',  'Arthritis', 'BP','Cancer', 'Cancer','Osteoporosis',  'Fibromyalgia', 'Alzheimers','My_Major_Symptom_1', 'My_Major_Symptom_2',
  #   ]
  # def __int__(self, *args, **kwargs):
  #       super(MajorsymverForm, self).__int__(*args, **kwargs)  ,


class MyfitnessForm(forms.ModelForm):

  class Meta:
    model = Myfitness
    fields = ['created_at','moderate_intensity', 'vigorous_intensity', 'muscle_build','balance']  
       
  
  def __init__(self, *args, **kwargs):
        super(MyfitnessForm, self).__init__(*args, **kwargs)
        

# class MyfitnessverForm(forms.ModelForm):

#   class Meta:
#      model=Myfitness_ver
#      fields = ['moderate_intensity', 'vigorous_intensity', 'muscle_build','balance']
#   def __init__(self, *args, **kwargs):
#         super(MyfitnessverForm, self).__init__(*args, **kwargs)
        

class MyfoodgroupsForm(forms.ModelForm):

    class Meta:
          model = Myfoodgroups
          fields = ['created_at','All_veggies', 'Beans_Lentils','Fruits_Berries','Protein', 'Dairy', 
            'Grains', 'Allergic1', 'Substitute1', 'Allergic2', 'Substitute2', 'Allergic3', 'Substitute3', ] 

    def __init__(self, *args, **kwargs):
             super(MyfoodgroupsForm, self).__init__(*args, **kwargs)

# class MyfoodgroupsverForm(forms.ModelForm):

#     class Meta:
#           model = Myfoodgroupsver
#           fields = ['Green_veggies',  'Red_Orange_veggies', 'Other_veggies','Fruits_Berries', 
#           'Protein', 'Dairy', 
#             'Grains',  'Herbs_Spices',] 

#     def __init__(self, *args, **kwargs):
#              super(MyfoodgroupsverForm, self).__init__(*args, **kwargs)            

# class MyfastfoodsForm(forms.ModelForm):

#     class Meta:
#           model = Myfastfoods
#           fields = ['Bacon','Burgers', 'Cookies', 'Cereals', 'Frozen_pizza', 'Ice_cream', 'Pancakes', 'Fried_foods', 'Popcorn', 
#            'Frozen_meals', 'Soft_drinks', 'Milk_shakes',  'Potato_chips', 'French_fries' 
#           ]  

 
#     def __init__(self, *args, **kwargs):
#             super(MyfastfoodsForm, self).__init__(*args, **kwargs)

            
            # self.fields['Bacon'].widget.attrs['style'] = 'font-size:18px; font-family: Arial, Helvetica, sans-serif; margin-bottom:35px'
           
            # self.fields['Burgers'].widget.attrs['style'] = 'font-size:18px; font-family: Arial, Helvetica, sans-serif; margin-bottom:35px'
            
            # self.fields['Cookies'].widget.attrs['style'] = 'font-size:18px; font-family: Arial, Helvetica, sans-serif; margin-bottom:35px'
            
            # self.fields['Cereals'].widget.attrs['style'] = 'font-size:18px; font-family: Arial, Helvetica, sans-serif; margin-bottom:35px'
            
            # # self.fields['Canned_foods'].widget.attrs['style'] = 'font-size:18px; font-family: Arial, Helvetica, sans-serif; margin-bottom:35px'

            # self.fields['Frozen_pizza'].widget.attrs['style'] = 'font-size:18px; font-family: Arial, Helvetica, sans-serif; margin-bottom:35px'
            
            # self.fields['Ice_cream'].widget.attrs['style'] = 'font-size:18px; font-family: Arial, Helvetica, sans-serif; margin-bottom:35px'
            
            # self.fields['Pancakes'].widget.attrs['style'] = 'font-size:18px; font-family: Arial, Helvetica, sans-serif; margin-bottom:35px'
            
            # self.fields['Popcorn'].widget.attrs['style'] = 'font-size:18px; font-family: Arial, Helvetica, sans-serif; margin-bottom:35px'
            
            # # self.fields['Margarine'].widget.attrs['style'] = 'font-size:18px; font-family: Arial, Helvetica, sans-serif; margin-bottom:35px'
            
            # # self.fields['Butter'].widget.attrs['style'] = 'font-size:18px; font-family: Arial, Helvetica, sans-serif; margin-bottom:35px'
            
            # self.fields['Frozen_meals'].widget.attrs['style'] = 'font-size:18px; font-family: Arial, Helvetica, sans-serif; margin-bottom:35px'
            
            # self.fields['Soft_drinks'].widget.attrs['style'] = 'font-size:18px; font-family: Arial, Helvetica, sans-serif; margin-bottom:35px'

            # self.fields['Milk_shakes'].widget.attrs['style'] = 'font-size:18px; font-family: Arial, Helvetica, sans-serif; margin-bottom:35px'


class MyfoodsuggestionsForm(forms.ModelForm):

    class Meta:
          model = Myfoodsuggestions
          fields = ['Salads', 'Sandwiches', 'Fruits_Berries', 'Dairy','Smoothies', 'Pasta', 'Soups',  'Oats', 'Egg_based', 
           'Grains','Soups','Beans_Legumes',  'Roti', 'Nuts_Seeds', 'Tacos_Burritos' ]


# class MyfastfoodsverForm(forms.ModelForm):

#     class Meta:
#           model = Myfastfoods_ver
#           fields = ['Bacon','Burgers', 'Cookies', 'Cereals', 'Frozen_pizza', 'Ice_cream', 'Pancakes', 'Fried_foods', 'Popcorn', 
#            'Frozen_meals', 'Soft_drinks', 'Milk_shakes',  'Potato_chips', 'French_fries' 
#           ]  

# class MyallergicfoodsForm(forms.ModelForm):

#     class Meta:
#           model = Myallergicfoods
#           fields = ['created_at','allergicFood1','allergicFood2','allergicFood3','allergicFood4','allergicFood5', 'allergicFood6', 'allergicFood7', 'allergicFood8',
#           'Food_substitute_1', 'Food_substitute_2', 'Food_substitute_3',  'Food_substitute_4', 'Food_substitute_5'
#             ]

#     def __init__(self, *args, **kwargs):
#             super(MyallergicfoodsForm, self).__init__(*args, **kwargs)   
               
# class MyallergicfoodsverForm(forms.ModelForm):

#     class Meta:
#           model = Myallergicfoods_ver
#           fields = ['Regular_Milk', 'Regular_Yogurt','Greek_Yogurt','Lactose_free_Milk','Peanuts', 'Walnuts', 'Pecans', 'Almonds', 
#           'Shell_fish', 'Fish', 'Soy', 'Eggs', 'Sesame', 'Wheat', 'Gluten_free_foods',
#           'Main_Food_1', 'Main_Food_2', 'Main_Food_3', 'Food_substitute_1', 'Food_substitute_2', 'Food_substitute_3'
#             ]

#     def __init__(self, *args, **kwargs):
#             super(MyallergicfoodsverForm, self).__init__(*args, **kwargs) 

# class MytrigfoodsForm(forms.ModelForm):

#     class Meta:
#       model = Mytrigfoods
#       fields = ['Trig_Food_1', 'Trig_Food_2', 'Trig_Food_3', 'Trig_Food_4', 'Foodtrig_substitute_1', 'Foodtrig_substitute_2', 'Foodtrig_substitute_3', 'Foodtrig_substitute_4',
#                'Trig_Drink_1', 'Trig_Drink_2',  'Trig_Drink_3',  'Drink_substitute_1', 'Drink_substitute_2', 'Drink_substitute_3' 
#           ]
#     def __int__(self, *args, **kwargs):
#             super(MytrigfoodsForm, self).__int__(*args, **kwargs) 


class Mytypmeals1Form(forms.ModelForm):
  
  class Meta:
    model = Mytypmeals1

    fields = [  'created_at','BCuisine1', 'B1_freq', 'Breakfast1',
              'LCuisine1', 'L1_freq',  'Lunch1',
              'DCuisine1', 'D1_freq', 'Dinner1',  

               'IngredientB11',  'IngredientB12',  'IngredientB13',  'IngredientB14',  'IngredientB15',  'IngredientB16',  'IngredientB17',  'IngredientB18',  
               'Ingredientbdr11', 'Ingredientbdr12', 'Ingredientbdr13', 'Ingredientbdr14',

               'IngredientL11',  'IngredientL12',  'IngredientL13',  'IngredientL14',  'IngredientL15',  'IngredientL16',  'IngredientL17',  'IngredientL18',  
               'Ingredientldr11', 'Ingredientldr12', 'Ingredientldr13', 'Ingredientldr14',

                'IngredientD11',  'IngredientD12',  'IngredientD13',  'IngredientD14',  'IngredientD15',  'IngredientD16',  'IngredientD17',  'IngredientD18',  
               'Ingredientddr11', 'Ingredientddr12', 'Ingredientddr13', 'Ingredientddr14',

               'Snack1', 'Snack1_freq', 'Snack2', 'Snack2_freq',

                 'Water_intake'
     ]
   
  
  def __init__(self, *args, **kwargs):
        super(Mytypmeals1Form, self).__init__(*args, **kwargs)



# class Mytypmeals2Form(forms.ModelForm):
  
#   class Meta:
#     model = Mytypmeals2

#     fields = [  'BCuisine', 'B_freq', 'Breakfast',
#               'LCuisine', 'L_freq',  'Lunch',
#               'DCuisine', 'D_freq', 'Dinner',  

#                'IngredientB11',  'IngredientB12',  'IngredientB13',  'IngredientB14',  'IngredientB15',  'IngredientB16',  'IngredientB17',  'IngredientB18',  
#                'Ingredientbdr11', 'Ingredientbdr12', 'Ingredientbdr13', 'Ingredientbdr14',

#                'IngredientL11',  'IngredientL12',  'IngredientL13',  'IngredientL14',  'IngredientL15',  'IngredientL16',  'IngredientL17',  'IngredientL18',  
#                'Ingredientldr11', 'Ingredientldr12', 'Ingredientldr13', 'Ingredientldr14',

#                 'IngredientD11',  'IngredientD12',  'IngredientD13',  'IngredientD14',  'IngredientD15',  'IngredientD16',  'IngredientD17',  'IngredientD18',  
#                'Ingredientddr11', 'Ingredientddr12', 'Ingredientddr13', 'Ingredientddr14',

#                'Snack1', 'Snack1_freq', 'Snack2', 'Snack2_freq',

#                  'Water_intake'
#      ]
   
  
#   def __init__(self, *args, **kwargs):
#         super(Mytypmeals2Form, self).__init__(*args, **kwargs)        
        

# class MylunchForm(forms.ModelForm):
  
#   class Meta:
#     model = Mylunch

#     fields = ['Cuisine1','Lunch1', 'L1_freq', 'lunch_source1', 
#     'Cuisine2','Lunch2', 'L2_freq', 'lunch_source2',
#     'Cuisine3','Lunch3', 'L3_freq', 'lunch_source3',
#     'Cuisine4','Lunch4', 'L4_freq', 'lunch_source4', ]
   
  
#   def __init__(self, *args, **kwargs):
#         super(MylunchForm, self).__init__(*args, **kwargs)

# class MydinnerForm(forms.ModelForm):
  
#   class Meta:
#     model = Mydinner

#     fields = ['Cuisine1','Dinner1', 'D1_freq', 'dinner_source1', 
#     'Cuisine2','Dinner2', 'D2_freq', 'dinner_source2',
#     'Cuisine3','Dinner3', 'D3_freq', 'dinner_source3',
#     'Cuisine4','Dinner4', 'D4_freq', 'dinner_source4', ]
   
  
#   def __init__(self, *args, **kwargs):
#         super(MydinnerForm, self).__init__(*args, **kwargs)


# class MytypicalmealsverForm(forms.ModelForm):
  
#   class Meta:
#     model = Mytypicalmeals_ver

#     fields = ['Breakfast1', 'IngredientB11', 'IngredientB12', 'IngredientB13', 'IngredientB14',
     
#      'Lunch1', 'IngredientL11', 'IngredientL12', 'IngredientL13', 'IngredientL14',  'Dinner1', 'IngredientD11', 
#      'IngredientD12', 'IngredientD13', 'IngredientD14', 'B1_freq', 'L1_freq', 'D1_freq' ]
#     # fields = "__all__"
  
#   def __init__(self, *args, **kwargs):
#         super(MytypicalmealsverForm, self).__init__(*args, **kwargs)

# class MycuisinemealsForm(forms.ModelForm):
  
#   class Meta:
#     model = Mycuisinemeals
 

#     fields = ['US_Generic', 'Chinese', 'Mexican', 'Thai', 'Indian', 'Italian', 'Mediterranean', 'Vietnamese', 'Japanese', 'Scrambled_eggs', 'Pancakes', 'Boiled_eggs', 
#     'Oatmeal', 'Fruit_juices', 'Non_beef_burgers', 'Salads', 'Omelettes', 'Bagels', 'Egg_salad_sandwich', 'Veggie_sandwich', 'Stirfry_noodles', 'Fried_Rice', 
#     'Sweet_sour_based', 'Hot_Sour_Soup', 'Egg_Drop_Soup', 'General_Tsos_based', 'Mogolian_based', 'Orange_sauce_based', 'Chinese_dumplings', 'Garlic_eggplant_sauce',
#      'Tacos', 'Fajitas', 'Migas', 'Quesadillas', 'Tortilla_soup', 'Enchiladas', 'Mexican_rice', 'Burritos', 'Burrito_bowl', 'Mexican_Soup', 'Pad_thai', 'Pumpkin_soup', 
#      'Thai_red_curry', 'Tom_Kha_soup', 'Thai_fried_rice', 'Spring_rolls', 'Tom_Yum_soup', 'Pineapple_fried_rice', 'Chick_peas_curry', 'Sambar', 'Aloo_gobi',
#      'Indian_Tomato_soup', 'Onion_Mushroom_curry', 'Tamarind_rice', 'Kidney_beans_curry', 'Tomato_Rasam_curry', 
     
#      'Okra_curry', 'Lemon_rice', 'Pepper_Garlic_Soup',
#      'Pulao', 'Eggplant_Parmesan', 'Pasta', 'Alfredo_noodles', 'Tortellini_soup', 'Minestrone_soup', 'Brushetta', 'Lasagna', 'Eggplant_sandwich']
     
    #  'Pho_soup',
    #  'Vietnamese_crepes', 'Avocado_smoothie', 'Vietnamese_curry', 'Banh_Mi', 'Jackfruit_smoothie', 'Vietnamese_stirfry', 'Tofu_tomato_sauce', 'Poke_Bowl',
    #  'Miso_soup', 'Eggplant_Donbury', 'Ramen_Noodles', 'Japanese_Curry', 'Grilled_Rice_balls', 'Brushetta_Tartines', 'Quinoa_salad', 'Lentil_Soup', 'Stuffed_Grape_leaves',
    #  'Chickpea_Burger', 'Caponata', 'Falafel', 'Spanish_potato_omelette'] 


# class MyeatoutmealsForm(forms.ModelForm):
  
#   class Meta:
#     model = Myeatoutmeals
#     fields = ['Breakfast1', 'IngredientB11', 'IngredientB12', 'IngredientB13', 'IngredientB14', 'IngredientB15', 'IngredientB16','Breakfast2', 'IngredientB21', 'IngredientB22', 'IngredientB23', 'IngredientB24', 'IngredientB25', 'IngredientB26',
#      'Lunch1', 'IngredientL11', 'IngredientL12', 'IngredientL13', 'IngredientL14', 'IngredientL15', 'IngredientL16', 'Lunch2', 
#      'IngredientL21', 'IngredientL22', 'IngredientL23', 'IngredientL24', 'IngredientL25', 'IngredientL26', 'Dinner1', 'IngredientD11', 
#      'IngredientD12', 'IngredientD13', 'IngredientD14', 'IngredientD15', 'IngredientD16', 'Dinner2', 'IngredientD21', 'IngredientD22', 
#      'IngredientD23', 'IngredientD24', 'IngredientD25', 'IngredientD26', 'Restaurant1', 'Restaurant2', 'Restaurant3', 'Restaurant4', 'Restaurant5', 'Restaurant6']

  
#   def __init__(self, *args, **kwargs):
#         super(MyeatoutmealsForm, self).__init__(*args, **kwargs)        


# class MyscheduleForm(forms.ModelForm):

#   class Meta:
#     model = Myschedule
#     fields = ['Meal_date1', 'Meal_date2', 'Meal_date3', 'Meal_date4', 'Meal_date5', 'Meal_date6', 
#     'Meal_date7', 'Fit_date1', 'Fit_date2', 'Fit_date3', 'Fit_date4', 'Fit_date5', 'Fit_date6', 
#     'Fit_date7']        


# class FruitberriesForm(forms.ModelForm):

#   class Meta:
#     model = fruitberries
#     fields = ['Apples', 'Apricot', 'Banana', 'Cantaloupe', 'Dates', 'Grapes', 'Guava', 'Kiwi', 'Mango', 
#     'Papaya', 'Pineapple', 'Plum', 'Peach', 'Blueberries', 'Blackberries', 'Cranberries',
#     'Cherries', 'Strawberries', 'Include_Apples', 'Include_Apricots', 'Include_Bananas', 'Include_Cantaloupe', 'Include_Dates', 'Include_Grapes', 'Include_Guava', 'Include_Kiwi', 'Include_Mango', 
#     'Include_Papaya', 'Include_Pineapple', 'Include_Plum', 'Include_Peach', 'Include_Blueberries', 'Include_Blackberries', 'Include_Cranberries',
#     'Include_Cherries', 'Include_Strawberries']

#     def __init__(self, *args, **kwargs):
#         super(FruitberriesForm, self).__init__(*args, **kwargs)


class SupplementsForm(forms.ModelForm):
  
  class Meta:
   model = Supplements
   fields = ['created_at','Supplement_1', 'Supplement_2', 'Supplement_3', 'Supplement_4', 'Supplement_5', ]     

# class SupplementsverForm(forms.ModelForm):
  
#   class Meta:
#    model = Supplements_ver
#    fields = ['created_at','Supplement_1', 'Supplement_2', 'Supplement_3', 'Supplement_4', 'Supplement_5', 'Supplement_6', 'Supplement_7', 
#    'Supplement_8', 'Supplement_9', 'Supplement_10']     
   
