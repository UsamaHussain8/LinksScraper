from . import views
from django.urls import path

urlpatterns = [
    path('scrape', views.render_links, name='web_scraper'),
    path('delete', views.delete_links, name='delete')
]
