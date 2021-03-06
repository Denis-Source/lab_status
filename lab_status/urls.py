from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.conf.urls import include

from api import urls as api_urls
from lab_user import urls as lab_user_urls
from event import urls as event_urls

from django.contrib import admin
from django.urls import path

from homepage.views import HomePageView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(api_urls)),
    path("events/", include(event_urls)),
    path("", include(lab_user_urls)),
    path("", HomePageView.as_view())
]

# map static files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
