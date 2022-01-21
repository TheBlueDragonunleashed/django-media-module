
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [


    path('logout/',views.logoutUser, name='logout'),
    # path('register/',views.registerUser, name='register'),
    path('',views.home, name='home'),
    path('room/',views.room, name='room'),
    path('lr/',views.lr, name='lr'),

    path("upload", views.send_files, name="uploads"),
    path('index/',views.index, name='index'),


    path('check',views.check, name='check'),
    path('add',views.add, name='add'),
    path('form',views.form, name='form'),
    # path('room/<str:pk>/',views.room, name='zbroom'),
    # path('create_room/',views.createRoom, name='create-room'),
    # path('update_room/<str:pk>',views.updateRoom, name='update-room'),
    # path('delete_room/<str:pk>',views.deleteRoom, name='delete-room'),
    # path('dhoom/',views.aamir, name='aamir'),

]
