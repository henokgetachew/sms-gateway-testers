from django.conf.urls import *

urlpatterns = patterns('',
                       url(r'^pushmobile-gateway-tester/$',
                           'sms_gateway_testers.views.pushmobile_gateway_tester',
                           name='pushmobile_gateway_tester')
                       )