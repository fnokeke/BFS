from django.conf.urls import url
from django.contrib import admin
from UssdApp.views import index
from ussd.views import AfricasTalkingUssdGateway


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^africastalking_gateway',
        AfricasTalkingUssdGateway.as_view(),
        name='africastalking_url'),
    url(r'^at',
        AfricasTalkingUssdGateway.as_view(),
        name='at')
]
