from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls', namespace='accounts')),
    path('', include('blogs.urls', namespace='blogs')),
    path('', include('core.urls', namespace='core')),
    path('', include('portfolio.urls', namespace='portfolio')),
]
