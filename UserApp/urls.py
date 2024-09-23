from django.urls import path
from . import views

urlpatterns = [
    path('',views.uhome,name='uhome'),
    path('uturf/<str:location>',views.uturf,name='uturf'),
    path('vmturf/<int:id>',views.vmturf,name='vmturf'),
    path('login',views.login,name='login'),
    path('uregister',views.uregister,name='uregister'),
    path('ureg',views.ureg,name='ureg'),
    path('chklogin',views.chklogin,name='chklogin'),
    path('userlogout',views.userlogout,name='userlogout'),
    path('bturf/<int:id>',views.bturf,name='bturf'),
    path('book',views.book,name='book'),
    path('bhistory',views.bhistory,name='bhistory'),
    path('contact',views.contact,name='contact'),
    path('feedback',views.feedback,name='feedback'),
]