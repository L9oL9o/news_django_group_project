from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  # Admin panel
                  path('admin/', admin.site.urls),

                  # App urls
                  path('', include('news_app.urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
