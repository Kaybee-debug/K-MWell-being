from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.register, name="register"),
    path('login/',views.logins, name="logins"),
    # path('logout/',views.logoutUser, name="logoutUser"), 
]