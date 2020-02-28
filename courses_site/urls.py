from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('courses/', include('courses.urls'), name='contacts'),
    path('contacts/', include('contacts.urls'), name='contacts'),
    path('api/', include('courses_api.urls'), name='api'),
    path('accounts/', include('accounts.urls'), name='accounts'),
    path('admin/', admin.site.urls),
    path('graphql/', include('courses_gql.urls'), name='graphql')

]