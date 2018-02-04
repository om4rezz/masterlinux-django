from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       url(r'^admin/', include(admin.site.urls)),

                       url(r'^$', 'subscriptions.views.home', name='home'),
                       url(r'^(?P<subscription_ref_id>.*)$', 'subscriptions.views.share', name='share'),
                       # url(r'^blog/', include('blog.urls')),

                       )
