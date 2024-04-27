from django.urls import path
from .views import index, contact, about, projects, success
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('contact/', contact, name='contact'),
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('projects/', projects, name='projects'),
    path('success/', success, name='success'),
]

# Add static files URL patterns
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)