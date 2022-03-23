"""
Proyecto Curso Django
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#
from django.contrib.sitemaps.views import sitemap
from applications.home.sitemap import EntrySiteMap, Sitemap

urlpatterns_mains = [
    path('admin/', admin.site.urls),
    path('', include('applications.users.urls')),
    path('', include('applications.home.urls')),
    path('', include('applications.entrada.urls')),
    path('', include('applications.favorito.urls')),
    #urls para ckeditor
    path(r'ckeditor/', include('ckeditor_uploader.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#Objeto site map que genera el xml
sitemaps = {
    'site': Sitemap(
        [
            'home_app:index'
        ]
    ),
    'entradas': EntrySiteMap
}

urlpatterns_sitemap = [ 
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name="django.contrib.sitemaps.views.sitemap")
]

urlpatterns = urlpatterns_mains + urlpatterns_sitemap