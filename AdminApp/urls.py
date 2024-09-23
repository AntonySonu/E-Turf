from django.urls import path
from . import views

urlpatterns = [
    path('ahome',views.ahome,name='ahome'),
    path('location',views.location,name='location'),
    path('linsert',views.linsert,name='linsert'),
    path('turfs',views.turfs,name='turfs'),
    path('tinsert',views.tinsert,name='tinsert'),
    path('vlocat',views.vlocat,name='vlocat'),
    path('ledit/<int:id>',views.ledit,name='ledit'),
    path('ldelete/<int:id>',views.ldelete,name='ldelete'),
    path('lupdate/<int:id>',views.lupdate,name='lupdate'),
    path('vturf',views.vturf,name='vturf'),
    path('vedit/<int:id>',views.vedit,name='vedit'),
    path('vdelete/<int:id>',views.vdelete,name='vdelete'),
    path('vupdate/<int:id>',views.vupdate,name='vupdate'),
    path('vmanager',views.vmanager,name='vmanager'),
    path('vamanager',views.vamanager,name='vamanager'),
    path('msupdate/<int:id>',views.msupdate,name='msupdate'),
    path('vuserbook',views.vuserbook,name='vuserbook'),
    path('vfeedback',views.vfeedback,name='vfeedback'),
    path('vusers',views.vusers,name='vusers'),
]