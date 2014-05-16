from django.conf.urls.defaults import *

urlpatterns = patterns('',
                       url(r'^pushmobile-gateway-tester/$',
                           'gateway_testers.views.pushmobile_gateway_tester',
                           name='pushmobile_gateway_tester')
                       )