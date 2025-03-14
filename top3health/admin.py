from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.db import models
# from .models import Healthsym
from .models import Myfitness
from .models import Myfoodgroups
from .models import Myfoodsuggestions
from .models import Study
from .models import Dietician
from .models import Supplements
from django.forms import TextInput, Textarea
from django.contrib.admin import AdminSite
from django.shortcuts import redirect



admin.site.site_header = "Dietician page"
    
# class CustomAdminSite(admin.AdminSite):

#     def get_user(self, request):
#         user = super().get_user(request)
#         if user and user.is_staff and not user.is_superuser: 
#             return redirect('dietician_dashboard') 
#         return user

# # Initialize the custom admin site
# admin_site = CustomAdminSite(name='myadmin')

# # Register your models with the custom admin site
# admin_site.register(CustomUser) 

# class CustomAdminSite(admin.AdminSite):

#     def index(self, request, extra_context=None):  # Override the index method
#         user = request.user  # Get the user from the request (already authenticated by admin)
#         if user.is_staff and not user.is_superuser:
#             return redirect('dietician_dashboard') # Redirect within the admin
#         return super().index(request, extra_context) # Default admin index

# admin_site = CustomAdminSite(name='myadmin')

# # # Register your models with the custom admin site
# admin_site.register(CustomUser) 


# class HealthsymInline(admin.StackedInline):
#     model = Healthsym
#     extra = 0 
#     fields = [
#         (('Minor1'), ('Minor2'), ('Minor3'), ('Minor4'), ('Minor5')),  
#         ('Major1', 'Major2', 'Major3', 'Major4', 'Major5'), 
#     ]

#     def has_view_permission(self, request, obj=None):
#         return request.user.groups.filter(name='Dietician').exists()

#     def has_change_permission(self, request, obj=None):
#         return request.user.groups.filter(name='Dietician').exists()

#     def has_delete_permission(self, request, obj=None):
#         return request.user.groups.filter(name='Dietician').exists()

#     formfield_overrides = {
#          models.CharField: {'widget': TextInput(attrs={'size':'0', 'style': 'margin-left:-100px;' 'margin-right:5px;''font-size: 12px;'  'font-style:bold'})},
#          models.TextField: {'widget': Textarea(attrs={'size':'0','rows':1, 'cols':40, 'style': 'margin-left:-100px;' 'font-size: 2px;'})},}      

# class FoodgroupsInline(admin.StackedInline):
#     model = Myfoodgroups
#     extra = 0 
#     fields = ['All_veggies', 'Beans_Lentils']

#     def has_view_permission(self, request, obj=None):
#         return request.user.groups.filter(name='Dietician').exists()

#     def has_change_permission(self, request, obj=None):
#         return request.user.groups.filter(name='Dietician').exists()

#     def has_delete_permission(self, request, obj=None):
#         return request.user.groups.filter(name='Dietician').exists()

# class FitnessInline(admin.StackedInline):
#     model = Myfitness
#     extra = 0 
#     fields = [('moderate_intensity', 'vigorous_intensity', 'muscle_build', 'balance')]

#     def has_view_permission(self, request, obj=None):
#         return request.user.groups.filter(name='Dietician').exists()

#     def has_change_permission(self, request, obj=None):
#         return request.user.groups.filter(name='Dietician').exists()

#     def has_delete_permission(self, request, obj=None):
#         return request.user.groups.filter(name='Dietician').exists()

#     formfield_overrides = {
#          models.CharField: {'widget': TextInput(attrs={'size':'10', 'style': 'margin-left:-100px;' 'margin-right:70px;' 'text-align:center'})},
#          models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':40, 'style': 'margin-left:0px;' 'margin-right:10px;' 'text-align:center'})}  }  

# class FoodsuggestionsInline(admin.StackedInline):
#     model = Myfoodsuggestions
#     extra = 0 
#     fields = [('Salads', 'Sandwiches', 'Fruits_Berries', 'Dairy'), ('Pasta', 'Egg_based', 'Grains', 'Soups'),('Oats','Beans_Legumes','Smoothies','Tacos_Burritos'),('Rice_based', 'Nuts_Seeds','Roti')]

#     def has_view_permission(self, request, obj=None):
#         return request.user.groups.filter(name='Dietician').exists()

#     def has_change_permission(self, request, obj=None):
#         return request.user.groups.filter(name='Dietician').exists()

#     def has_delete_permission(self, request, obj=None):
#         return request.user.groups.filter(name='Dietician').exists()

#     formfield_overrides = {
#          models.CharField: {'widget': TextInput(attrs={'size':'10', 'style': 'margin-left:-10px;' 'margin-right:30px;'})},
#          models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':40, 'style': 'margin-left:-50px;'})},}    

# class SupplementsInline(admin.StackedInline):
#     model = Supplements
#     extra = 0 
#     fields = [('Supplement_1', 'Supplement_2', 'Supplement_3'),('Supplement_4', 'Supplement_5')]

#     def has_view_permission(self, request, obj=None):
#         return request.user.groups.filter(name='Dietician').exists()

#     def has_change_permission(self, request, obj=None):
#         return request.user.groups.filter(name='Dietician').exists()

#     def has_delete_permission(self, request, obj=None):
#         return request.user.groups.filter(name='Dietician').exists()

#     formfield_overrides = {
#          models.CharField: {'widget': TextInput(attrs={'size':'10', 'style': 'margin-left:-100px;' 'margin-right:50px;'})},
#          models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':40, 'style': 'margin-left:-100px;'})},}    


# class UserAdmin(UserAdmin):
#     list_display = (('username', 'first_name', 'last_name', ))
#     list_filter = ()
#     # field_sets = ('password', 'is_staff','last_login', 'date_joined',  'permissions', 'is_superuser', 'last_name', 'first_name', 'email')

#     inlines = [HealthsymInline, FoodgroupsInline, FitnessInline, FoodsuggestionsInline, SupplementsInline]        

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Myfoodgroups)
admin.site.register(Myfitness)
# admin.site.register(Healthsym)
admin.site.register(Myfoodsuggestions)
admin.site.register(Supplements)
admin.site.register(Dietician)


# class HealthsymInline(admin.StackedInline):
#     model = Healthsym
#     extra = 0 
#     fields = [
#         ('Minor1', 'Minor2', 'Minor3', 'Minor4', 'Minor5'),  
#         ('Major1', 'Major2', 'Major3', 'Major4', 'Major5'), 
#     ]

#     def has_view_permission(self, request, obj=None):
#         if request.user.is_superuser:  # Only superusers have unrestricted view
#             return True 
#         elif request.user.is_staff and request.user.groups.filter(name='Dietician').exists():
#             return True 
#         return False 

#     def has_change_permission(self, request, obj=None):
#         if request.user.is_superuser: 
#             return True 
#         return False 

#     def has_delete_permission(self, request, obj=None):
#         if request.user.is_superuser: 
#             return True 
#         return False 

#     formfield_overrides = {
#         models.CharField: {'widget': TextInput(attrs={'size':'10', 'style': 'margin-left:-70px; margin-right:20px;'})}, 
#         models.TextField: {'widget': Textarea(attrs={'rows':2, 'cols':30, 'style': 'margin-left:-50px;'})}, 
#     }

# class FoodgroupsInline(admin.StackedInline):
#     model = Myfoodgroups
#     extra = 0  # Optional: Show an extra empty form for adding new Healthsym instances
#     fields = [
#         ('All_veggies', 'Fruits_Berries', 'Protein', 'Dairy', 'Grains', 'Beans_Lentils'),  
#     ]


#     formfield_overrides = {
#         models.CharField: {'widget': TextInput(attrs={'size':'20', 'style': 'margin-left:-90px;' 'margin-right:30px;'})},
#         models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':6, 'style': 'margin-left:-50px;'})},
#     }     

# class FitnessInline(admin.StackedInline):
#     model = Myfitness
#     extra = 0  # Optional: Show an extra empty form for adding new Healthsym instances
#     fields = [
#         ('moderate_intensity', 'vigorous_intensity', 'muscle_build', 'balance'),  
#     ]

#     formfield_overrides = {
#         models.CharField: {'widget': TextInput(attrs={'size':'10', 'style': 'margin-left:-100px;' 'margin-right:70px;' 'text-align:center'})},
#         models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':40, 'style': 'margin-left:0px;' 'margin-right:10px;' 'text-align:center'})},
#     }

# class FoodsuggestionsInline(admin.StackedInline):
#     model = Myfoodsuggestions
#     extra = 0  # Optional: Show an extra empty form for adding new Healthsym instances
#     fields = [
#         ('Salads', 'Smoothies', 'Fruits_Berries', 'Dairy', 'Oats',  'Nuts_Seeds','Tacos_Burritos', 'Egg_based', 'Sandwiches','Pasta', 'Soups','Beans_Legumes', 'Rice_based', 'Grains','Roti'),  
#     ]


#     formfield_overrides = {
#         models.CharField: {'widget': TextInput(attrs={'size':'10', 'style': 'margin-left:-100px;' 'margin-right:30px;'})},
#         models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':40, 'style': 'margin-left:-50px;'})},
#     }


   
    # fields = [
    #     ('first_name', 'last_name',  'Gender',  'dob'), ('Height_ft', 'Height_in', 'Weight_in_pounds',) ]

    # def get_fields(self, request, obj=None):
    #     if request.user.is_superuser:
    #         return ['username'
    #             ]    
    #     else:
    #         return [('first_name', 'last_name',  'Gender',  'dob'), ('Height_ft', 'Height_in', 'Weight_in_pounds',)] 
    # formfield_overrides = {
    #     models.CharField: {'widget': TextInput(attrs={'size':'10', 'style': 'margin-left:-80px;' 'margin-right:20px;'})},
    #     models.TextField: {'widget': Textarea(attrs={'rows':2, 'cols':30, 'style': 'margin-left:-50px;' })},
    # }    