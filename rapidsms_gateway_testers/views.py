from django.http import HttpResponse
from django.template import loader, RequestContext
from django.contrib.auth.decorators import login_required
from rapidsms_gateway_testers.pushmobile_incoming_simulation import simulate_incoming_message
import rapidsms_gateway_testers.settings


@login_required
def pushmobile_gateway_tester(request):
    target_url = rapidsms_gateway_testers.settings.PUSH_MOBILE_GATEWAY_TARGET_URL

    if request.method == 'POST':
        msg = request.POST.get('msg')
        phone_no = request.POST.get('phone_no')
        simulate_incoming_message(target_url, phone_no, msg)

    t = loader.get_template('pushmobile-gateway-tester.html')
    c = RequestContext(request)
    return HttpResponse(t.render(c))