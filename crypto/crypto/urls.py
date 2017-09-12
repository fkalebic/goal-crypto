from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Examples:
    # url(r'^$', 'crypto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^usermanagement/', include('usermanagement.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login'}),
]
