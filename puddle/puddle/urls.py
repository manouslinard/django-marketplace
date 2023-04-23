from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.views import index, contact
from item import urls as item_urls


urlpatterns = [
    path("", index, name="index"),
    path("items/", include(item_urls)),
    path("contact/", contact, name="contact"),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
