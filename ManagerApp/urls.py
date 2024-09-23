from django.urls import path
from . import views

urlpatterns = [
    path('mreg',views.mreg,name='mreg'),
    path('mhome',views.mhome,name='mhome'),
    path('managerlogout',views.managerlogout,name='managerlogout'),
    path('mprofile',views.mprofile,name='mprofile'),
    path('mreginsert',views.mreginsert,name='mreginsert'),
    path('mvturfs/<str:location>',views.mvturfs,name='mvturfs'),
    path('mvmturf/<int:id>',views.mvmturf,name='mvmturf'),
    path('massignturf',views.massignturf,name='massignturf'),
    path('mturfbook',views.mturfbook,name='mturfbook'),
    path('approve/<int:id>',views.approve,name='approve'),
    path('decline/<int:id>',views.decline,name='decline'),
]