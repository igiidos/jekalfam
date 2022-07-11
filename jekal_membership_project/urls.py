from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index_app.urls')),
    path('membership_app/', include('membership_app.urls')),
    path('my/', include('personal_app.urls')),
    # path('accounts/', include('accounts.urls')),
]
