from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^main', hello.views.main, name='main'),
    url(r'^teapot', hello.views.teapot, name='teapot'),
    url(r'^teapot2', hello.views.teapot, name='teapot2'),
    url(r'^drinks', hello.views.drinks, name='drinks'),
    url(r'^categories', hello.views.categories, name='categories'),
    path('admin/', admin.site.urls),
]
