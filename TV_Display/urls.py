from django.urls import path 
from . import views

urlpatterns = {
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('home2',views.home2,name='home2'),
    path('home3',views.home3,name='home3'),
    path('hindi',views.hindi,name='hindi'),
    path('hindi2',views.hindi2,name='hindi2'),
    path('marathi',views.marathi,name='marathi'),
    path('tv_java',views.tv_java,name='tv_java'),
    path('NTES_TV',views.ntes_display_format,name='NTES_TV'),
    path('NTES_TV_J',views.ntes_display_java,name='NTES_TV_J'),
    path('login',views.login,name='login'),
    path('10Line',views.tenline,name='10Line'),
    path('10LineH',views.tenlineH,name='10LineH'),
    path('10LineM',views.tenlineM,name='10LineM'),    
}