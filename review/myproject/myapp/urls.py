from django.urls import path
from myapp import views
urlpatterns = [
    path('sample',views.index),
    path('html',views.htmlpro)
]

