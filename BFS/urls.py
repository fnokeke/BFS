from django.conf.urls import url
from django.contrib import admin

from UssdApp.views import CustomUssdView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$', index),
    url(r'^$', CustomUssdView.as_view(), name='index_africastalking'),
    url(r'^africastalking_gateway', CustomUssdView.as_view(), name='africastalking_url'),
]


