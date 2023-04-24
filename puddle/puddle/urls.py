from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from item import urls as item_urls


urlpatterns = [
    path("", include('core.urls')),
    path("items/", include(item_urls)),
    path("admin/", admin.site.urls),
    path("dashboard/", include('dashboard.urls')),
    path("inbox/", include('conversation.urls')),
    path('verification/', include('verify_email.urls')),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
