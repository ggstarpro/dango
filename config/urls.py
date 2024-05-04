"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView
# from django.urls import path
from django.urls import path, include
from mysite import views
from django.views.decorators.cache import cache_page

# -- for サイトマップ --
from django.contrib.sitemaps.views import sitemap
from config.sitemaps import StaticViewSitemap, BlogSiteMap
sitemaps = {
    "static": StaticViewSitemap,
    "blog": BlogSiteMap,
}

"""
This XML file does not appear to have any style information associated with it. The document tree is shown below.
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
    <script />
    <url>
        <loc>http://127.0.0.1:8080/</loc>
        <changefreq>daily</changefreq>
        <priority>0.5</priority>
    </url>
    <url>
        <loc>http://127.0.0.1:8080/langding_mui/</loc>
        <changefreq>daily</changefreq>
        <priority>0.5</priority>
    </url>
    <url>
        <loc>http://127.0.0.1:8080/blog/1/</loc>
        <lastmod>2024-04-24</lastmod>
        <changefreq>daily</changefreq>
        <priority>0.5</priority>
    </url>
    <url>
        <loc>http://127.0.0.1:8080/blog/2/</loc>
        <lastmod>2024-04-24</lastmod>
        <changefreq>daily</changefreq>
        <priority>0.5</priority>
    </url>
    <url>
        <loc>http://127.0.0.1:8080/blog/3/</loc>
        <lastmod>2024-04-28</lastmod>
        <changefreq>daily</changefreq>
        <priority>0.5</priority>
    </url>
    <url>
        <loc>http://127.0.0.1:8080/blog/4/</loc>
        <lastmod>2024-04-29</lastmod>
        <changefreq>daily</changefreq>
        <priority>0.5</priority>
    </url>
    <url>
        <loc>http://127.0.0.1:8080/blog/5/</loc>
        <lastmod>2024-04-29</lastmod>
        <changefreq>daily</changefreq>
        <priority>0.5</priority>
    </url>
</urlset>
"""
# -- for サイトマップ --

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('', include('mysite.urls')),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
]
