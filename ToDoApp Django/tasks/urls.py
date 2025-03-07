from django.urls import path
from .import views

urlpatterns=[
    path('',views.index,name='list'),

    path('update/<str:pk>/',views.updatetask,name='updatetask1'),

    path('delete/<str:pk>/',views.deletetask,name='deletetask1'),

]