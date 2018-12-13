"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from UssdApp.views import index, helloworld, maxy
from ussd.views import AfricasTalkingUssdGateway


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'hw/$', helloworld),
    url(r'maxy/$', maxy),
    url(r'^africastalking_gateway',
        AfricasTalkingUssdGateway.as_view(),
        name='africastalking_url'),
    url(r'^at',
        AfricasTalkingUssdGateway.as_view(),
        name='at')
]
