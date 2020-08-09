from django.contrib import admin
from django.urls import path, include

from puppies import urls as puppies_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path("puppies/", include(puppies_urls))
]
