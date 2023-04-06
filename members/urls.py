from django.urls import path
from . import views

urlpatterns = [
    path('',views.main,name='main'),
    path('portfolio/',views.portfolio,name='port'),
    path('testdata/',views.testing2,name='test2'),
    path('testing/',views.testing,name='testing'),     
    path('members/', views.members, name='members'),
    path('members/details/<int:id>',views.details,name='details')
]