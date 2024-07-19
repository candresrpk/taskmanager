
from django.contrib import admin
from django.urls import path, include
from .views import HomePage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage, name='home'),
    path('users/', include('users.urls')),
    path('tasks/', include('tasks.urls')),
]
