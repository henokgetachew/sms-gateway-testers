from django.http import HttpResponse
from django.template import loader, RequestContext
from rapidsms_gateway_testers.pushmobile_send_simulation import simulate_send_message

target_url = "http://127.0.0.1:8000/pushmobile/?"

def pushmobile_gateway_tester (request):
    
    if request.method == 'POST':
        msg = request.POST.get('msg')
        phone_no = request.POST.get('phone_no')
        simulate_send_message(target_url, phone_no,msg)        
    
    t = loader.get_template('pushmobile-gateway-tester.html')
    c = RequestContext(request)
    return HttpResponse(t.render(c))