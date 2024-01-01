from django.contrib import admin
from django.urls import path, include  # Make sure 'include' is imported

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('polls.urls')),  # Ensure this line includes the 'polls' app URLs for the root path
    # ... other paths ...
]