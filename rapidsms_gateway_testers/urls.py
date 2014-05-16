from django.conf.urls import *

urlpatterns = patterns('',
                       url(r'^pushmobile-gateway-tester/$',
                           'rapidsms_gateway_testers.views.pushmobile_gateway_tester',
                           name='pushmobile_gateway_tester')
                       )