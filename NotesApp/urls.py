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
from login.views import home_view,public_view,private_view,about_view,publish_view,support_view,contact_view,login_view,register_view,logoutUser,notes_view,update_view,delete_view,print_view,insight_view,documents_view,doc_view,video_view,audio_view,image_view,go_back_view
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', home_view, name='home'),
    # path('contact/', contact_view),
    path('admin/', admin.site.urls),
    path('login/',login_view, name='login_page'),
    path('logout/',logoutUser,name='logout_page'),
    path('register/',register_view, name='register'),
    path('notes/',notes_view, name='notes_page'),
    path('update_page/<str:pk>/',update_view, name='update_page'),
    path('delete_page/<str:pk>/',delete_view, name='delete_page'),
    path('print_page/<str:pk>/',print_view, name='print_page'),
    path('insight_page/<str:pk>/',insight_view, name='insight_page'),
    path('documents_page/<str:pk>/',documents_view, name='documents_page'),
    path('doc_page/<str:pk>/',doc_view, name='doc_page'),
    path('video_page/<str:pk>/',video_view, name='video_page'),
    path('audio_page/<str:pk>/',audio_view, name='audio_page'),
    path('image_page/<str:pk>/',image_view, name='image_page'),
    path('about/',about_view, name='about'),
    path('support/',support_view, name='support'),
    path('publish/<str:pk>/',publish_view, name='publish'),
    path('notes/public_all',public_view, name='public_all'),
    path('private/<str:pk>/',private_view, name='private'),
    




]
urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

