from django.conf.urls import include, url
from django.contrib import admin

import blog.urls
from blog import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^', include(blog.urls)),
    url(r'^admin/', include(admin.site.urls)),
]