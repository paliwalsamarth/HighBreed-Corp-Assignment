from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('appsearch/', include(('appsearch.urls', 'appsearch'), namespace='appsearch')),
    path('keyfinder/', include(('keyfinder.urls', 'keyfinder'), namespace='keyfinder')),
    path('', include(('homeapp.urls', 'homeapp'), namespace='homeapp')),
    # path('', include(('appsearch.urls', 'appsearch'), namespace='appsearch')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
