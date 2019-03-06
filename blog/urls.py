from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^(?P<pk>\d+)/$', views.EntryDetail.as_view(), name='entry_detail'),
]
