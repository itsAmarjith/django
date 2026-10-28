urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('secondapp.urls'))
]