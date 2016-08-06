from django.conf.urls import url
from disputes.views import index_view, dispute, resolve, landing

urlpatterns = [
    url(r'^$', index_view, name='index_view'),
    url(r'^landing$', landing, name='landing'),
    url(r'^dispute$', dispute, name='dispute'),
    url(r'^resolve$', resolve, name='resolve'),
]
