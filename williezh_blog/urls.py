from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib import admin
from django.contrib.sitemaps.views import index
from django.contrib.sitemaps.views import sitemap
from django.views.defaults import bad_request
from django.views.defaults import page_not_found
from django.views.defaults import permission_denied
from django.views.defaults import server_error
from django.views.generic.base import RedirectView
from django.views.static import serve
from django_xmlrpc.views import handle_xmlrpc

from zinnia.sitemaps import AuthorSitemap
from zinnia.sitemaps import CategorySitemap
from zinnia.sitemaps import EntrySitemap
from zinnia.sitemaps import TagSitemap

urlpatterns = [
#    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r'^$', RedirectView.as_view(url='/blog/', permanent=True),name='home'),
    url(r'^blog/', include('zinnia.urls', namespace='zinnia')),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^xmlrpc/$', handle_xmlrpc),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("account.urls")),
    url(r"^account/social/accounts/$", TemplateView.as_view(
        template_name="account/social.html"), name="account_social_accounts"),
    url(r"^account/social/", include("social_django.urls", namespace="social")),
]

sitemaps = {
    'tags': TagSitemap,
    'blog': EntrySitemap,
    'authors': AuthorSitemap,
    'categories': CategorySitemap
}

urlpatterns += [
    url(r'^sitemap.xml$',
        index,
        {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$',
        sitemap,
        {'sitemaps': sitemaps}),
]

urlpatterns += [
    url(r'^400/$', bad_request),
    url(r'^403/$', permission_denied),
    url(r'^404/$', page_not_found),
    url(r'^500/$', server_error),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT})
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
