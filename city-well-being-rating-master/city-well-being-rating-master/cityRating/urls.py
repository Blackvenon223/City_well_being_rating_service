from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('cityRatingapp/', include('cityRatingapp.urls')),
    path('admin/', admin.site.urls),
]
