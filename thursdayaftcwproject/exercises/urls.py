from django.urls import path

from . import views

urlpatterns = [
    path('children/', views.listChildrenAndMom, name='Child'),
    path('moms/', views.listAllChildren, name='Mom'),
    path('addchild/', views.addAChild, name='add'),
    path('deletemom/', views.deletemom, name='delete'),
]