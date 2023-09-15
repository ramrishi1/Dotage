"""
URL configuration for DotAge project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name= 'about' ),
    path('events/', views.events, name= 'events'),
    path('users/', views.users, name= 'users'),
    path('loginpage/', views.loginpage, name= 'loginpage'),
    path('signupage/', views.signupage, name= 'signupage'),
    path('eventcreation/', views.eventcreation, name= 'eventcreation'),
    path('afterlogin/', views.afterlogin, name= 'afterlogin'),
    path('eventslogin/', views.eventslogin, name= 'eventslogin'),
    path('signup/', views.signup, name= 'signup'),
    path('registerpage/<int:id>', views.registerpage, name= 'registerpage'),
    path('register/<int:id>', views.register, name= 'register'),
    path('login/', views.login, name= 'login'),
    path('logout/', views.logout, name= 'logout'),
    path('profile/', views.profile, name= 'profile'),
    # path('update_profile_picture/', views.update_profile_picture, name='update_profile_picture'),
    path('editprofile/', views.editprofile, name= 'editprofile'),
    path('eventsafterlogin/', views.eventsafterlogin, name= 'eventsafterlogin'),
    path('usersafterlogin/', views.usersafterlogin, name= 'usersafterlogin'),
    # path('eventdetails/', views.eventdetails, name= 'eventdetails'),
    path('event/<int:event_id>/', views.eventdetails, name='eventdetails'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

