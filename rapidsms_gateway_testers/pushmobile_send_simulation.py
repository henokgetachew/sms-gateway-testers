import random
from random import randint
import datetime
from xml.sax.saxutils import escape
import urllib2
from django.template import loader, Context

incoming_template_name = 'pushmobile-incoming-template.xml'


def simulate_send_message(target_url, number, text):
    msg_id = randint(1, 99999)
    time_sent = datetime.datetime.now()
    loc = random.randint(1, 99999)
    ntk = random.choice(['vodafone', 'mtn', 'safaricom'])

    params = {"text": escape(text),
              "mobile_number": number,
              "message_id": msg_id,
              "time_stamp": time_sent,
              "local": loc,
              "mobile_network": ntk,
    }

    messaging_template = loader.get_template(incoming_template_name)
    messaging_context = Context(params, True, None, None, None)

    payload = messaging_template.render(messaging_context)

    print ('Payload: %s' % payload)

    req = urllib2.Request(url=target_url,
                          data=payload,
                          headers={'Content-Type': 'application/xml'})

    handle = urllib2.urlopen(req)
    resp = handle.read()
    return "response: %s" % resp
