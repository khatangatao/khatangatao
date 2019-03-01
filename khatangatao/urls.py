from django.conf.urls import include, url
from django.contrib import admin

# static files
from django.conf import settings
from django.conf.urls.static import static


import blog.urls
from blog import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^', include(blog.urls)),
    url(r'^authors/', views.AuthorList.as_view(), name='authors'),
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += [
    url(r'^catalog/', include('catalog.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
