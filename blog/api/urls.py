from django.conf.urls import include, url
from ..views import EntryApi
from rest_framework import routers


router = routers.DefaultRouter()
router.register('entry', EntryApi, base_name='entry')

urlpatterns = [
    # API
    url(r'^', include(router.urls)),
]