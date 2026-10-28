from django.urls import path
from myapp import views
urlpatterns = [
     path('',views.index),
     path('html',views.htmlpro),
     path('home',views.htmlmod)
]
