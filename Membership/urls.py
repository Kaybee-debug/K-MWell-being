from django.urls import path
from . import views
urlpatterns = [
    path('detail/',views.member_create, name="member_create"),
    # path('login/',views.logins, name="logins"),
    # path('logout/',views.logoutUser, name="logoutUser"), 
]