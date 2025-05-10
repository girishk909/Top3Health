from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .views import SignUpView
from django.views.generic import TemplateView
from .views import MyLoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import PasswordChangeDoneView
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetCompleteView
from django.views.generic import RedirectView

from .views import my_view
from .views import flashpageView
from .views import BeginpageView

# from .views import customroleView
from .views import HomePageView
from .views import LandingView
from .views import MyfitnessView
from .views import MyfitnessUpdateView
from .views import MyfoodgroupsView
from .views import MyfoodgroupsverView
from .views import MysettingsView
from .views import MybreakfastdesignView
from .views import MyhabitsupdateView

from .views import MysupplementsView

from .views import MinorsymView
from .views import MinorsymUpdateView

# from .views import MyfastfoodsUpdateView

from .views import DailylogView

from .views import MyexpensesView
from .views import MymonthlyexpensesView
from .views import MyhabitsView

from .views import MyHealthscreeningView
from .views import MyHealthscreeningUpdateView
from .views import MyyearlyHealthscreeningUpdateView
from django.contrib import admin
from .views import list_users
from .views import MyfoodsuggestionsView
from .views import MysuggestionsView
from .views import testauthview
from .views import dietician_dashboard
from .views import HealthlinksView


urlpatterns = [    
    path('', HomePageView.as_view(), name='top3health-bootstrap'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('dietician_dashboard/', list_users, name='dietician_dashboard'),
    path('flashpage/', flashpageView.as_view(), name='flashpage'),
    path('myfoodgroups/', MyfoodgroupsView, name='myfoodgroups'),
    # path('staff_register/', views.staff_register, name='staff_register'),  
    path('logout', HomePageView.as_view(), name='top3health-bootstrap'),
    path('test_auth', testauthview, name='test_auth'),
    path('signup/', SignUpView, name='signup'),
    # path('landing/', LandingView.as_view(), name='landing'),
    path('begindate/', BeginpageView, name='begindate'),
    path('weekly_suggestions/', MysuggestionsView, name='weekly_suggestions'),
    path('healthinfo/', HealthlinksView.as_view(), name='healthinfo'),
    path('myfoodsuggestions/', MyfoodsuggestionsView, name='myfoodsuggestions'),
    path('Dailylog/', DailylogView, name='Dailylog'),
    path('myhealthscreening/', MyHealthscreeningView, name='myhealthscreening'),
    path('healthscreeningupdate', MyHealthscreeningUpdateView, name='healthscreeningupdate'),
    path('yearlyhealthscreening',MyyearlyHealthscreeningUpdateView, name='yearlyhealthscreening'),
    path('minorsym/', MinorsymView, name='minorsym'),
    path('minorsymupdate/', MinorsymUpdateView, name='minorsymupdate'),
    path('myfitness/', MyfitnessView, name='myfitness'),
    path('settings/', MysettingsView, name='settings'),
    path('myexpenses/', MyexpensesView, name='myexpenses'),    
    path('myexpensesupdate/',MymonthlyexpensesView, name='myexpensesupdate'),    
    path('myhabits/', MyhabitsView, name='myhabits'),
    path('myhabitsupdate/', MyhabitsupdateView, name='myhabitsupdate'),
    path('mybreakfastdesign', MybreakfastdesignView, name='mybreakfastdesign'),
    # path('myfoodsuggestions/', MyfoodsuggestionsView, name='myfoodsuggestions'),
    path('supplements/', MysupplementsView, name='supplements'),
    path('landing/', views.health_dashboard, name='landing'),
    path('reports/', views.incoming_dashboard, name='reports'),
   

    # path('admin/', admin.site.urls),
    ]

         

