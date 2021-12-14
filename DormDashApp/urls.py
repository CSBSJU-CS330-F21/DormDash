from django.urls import path
from . import views
from .views import profile, restaurant_list
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from DormDashApp.views import logoutUser


# URLConf
urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name = 'signup'),
    path('createCustomer/', views.CustomerSignUpView.as_view(),name="createCustomer"),
    path('createDriver/', views.DriverSignUpView.as_view(),name="createDriver"),
    path('', views.loginUser),
    path('restaurant_list/', views.restaurant_list, name="restaurant_list"),
    path('logout/', views.logoutUser, name="logout"),
    path('login/', views.loginUser, name="login"),
    path('profile/', profile, name='profile'),
    path('editprofile/', views.ProfileChangeView.as_view(), name='editprofile'),
    path('deleteprofile/', views.ProfileDeleteView.as_view(), name='deleteprofile'),
    path('driverorders/',views.driverorders, name='driverorders'),
    path('orderdetails/',views.orderdetails, name='orderdetails'),
    path('menu_list/', views.menu_list, name="menu_list"),


]
urlpatterns += staticfiles_urlpatterns()