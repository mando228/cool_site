from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Cool_Site.urls')),
    path('captcha/', include('captcha.urls')),
    path("__debug__/", include("debug_toolbar.urls")),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
