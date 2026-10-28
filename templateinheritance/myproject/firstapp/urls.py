from django.urls import path
from firstapp import views
urlpatterns = [
    path('',views.html_pro,name='home'),
    path('svc',views.service,name='svc')
]
