from django.urls import path
from . import views

urlpatterns = [
    path('',views.projects,name='projects'),
    #dynamic URL creation
    path('project/<str:pk>',views.project,name='project')
]