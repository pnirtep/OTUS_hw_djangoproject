from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('courses/', include('courses.urls')),
    path('contacts/', include('contacts.urls')),
<<<<<<< HEAD:courses_site/courses_site/urls.py
=======
    path('api/', include('courses_api.urls')),
>>>>>>> courses api add:courses_site/urls.py
    path('admin/', admin.site.urls),


]