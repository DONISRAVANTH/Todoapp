from django.urls import path
from . import views

urlpatterns = [
    path('',views.Addtask,name='Addtask'), 
    path('update/<int:pk>',views.update_task,name='update_task'),
    path('delete/<int:pk>',views.delete,name='delete'),  
]