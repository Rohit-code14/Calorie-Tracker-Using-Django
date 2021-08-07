from django.urls import path
from .views import HomePageView,LoginPage,LogOutPage,select_food,add_food,RegisterPage,ProfilePage,update_food,delete_food
urlpatterns = [
    #home route
    path('', HomePageView,name='home'),

    #Auth Routes
    path('login/',LoginPage,name='login'),
    path('logout/',LogOutPage,name='logout'),

    #CRUD Operation routes
    path('select_food/',select_food,name='select_food'),
    path('add_food/',add_food,name='add_food'),
    path('update_food/<str:pk>/',update_food,name='update_food'),
    path('delete_food/<str:pk>/',delete_food,name='delete_food'),
    
    #user registration and profile info routes
    path('register/',RegisterPage,name='register'),
    path('profile/',ProfilePage,name='profile'),
]