"""NotesApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from login.views import home_view,contact_view,login_view,register_view,logoutUser,notes_view,update_view,delete_view
urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_view),
    path('admin/', admin.site.urls),
    path('login/',login_view, name='login_page'),
    path('logout/',logoutUser,name='logout_page'),
    path('register/',register_view, name='register'),
    path('notes/',notes_view, name='notes_page'),
    path('update_page/<str:pk>/',update_view, name='update_page'),
    path('delete_page/<str:pk>/',delete_view, name='delete_page'),

]

