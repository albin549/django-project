from django.urls import path

from new_app import views

urlpatterns = [
    path('',views.home, name= "home"),
    path('index', views.index,name= 'index'),
    path('wolf',views.wolf,name= 'wolf')
]