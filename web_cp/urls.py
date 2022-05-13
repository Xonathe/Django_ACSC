from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.main, name='login'),
    path('', views.profile, name='profile'),
    path('add_data/', views.add_data, name='add_data'),
    path('logs/', views.logs, name='logs'),
    path('logout/', views.log_out, name='logout'),
]
