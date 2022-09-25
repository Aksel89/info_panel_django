from django.contrib import admin
from django.urls import path, include
from info_panel.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('info_panel.urls')),
]
