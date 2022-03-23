from django.contrib.sitemaps import Sitemap
from datetime import datetime, timedelta

from django.urls import reverse_lazy

from applications.entrada.models import Entry

class EntrySiteMap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = "https"

    def items(self):
        return Entry.objects.filter(public=True)

    def lastmod(self, obj):
        return obj.created

class Sitemap(Sitemap):
    protocol = "https"
    
    def __init__(self, names):
        self.names = names

    def items(self):
        return self.names

    def changefreq(self, obj):
        return 'Weekly'
        
    def lastmod(self, obj):
        return datetime.now()

    def location(self, obj):
        return reverse_lazy(
            'home_app:index'
        )