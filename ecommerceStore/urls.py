from django.contrib import admin
from django.urls import path, include
import debug_toolbar
from playground.views import home


admin.site.site_header = 'Store Admin'
admin.site.index_title = 'Admin'

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('store/', include('store.urls'))
]
