from django.conf.urls import url
from disputes.views import index_view

urlpatterns = [
    url(r'^$', index_view, name='index_view'),
]
