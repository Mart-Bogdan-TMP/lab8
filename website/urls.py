from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^info/', include('taxistation.urls')),
    url(r'^tables/', include('tables.urls')),
]
