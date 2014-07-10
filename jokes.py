#!/usr/bin/python

from twilio.rest import TwilioRestClient
from twilio import TwilioRestException
from apscheduler.scheduler import Scheduler
from requests import get

ACCOUNT_SID = "AC28f3d3e0ace40f8421f70f11930d7eed"
AUTH_TOKEN = "5a2cb13b0e34f20e92b7b57856d19e72"
CLIENT = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

def send_message(content):
    '''
    Wrapper function which calls Twilio API
    '''
    try:
        CLIENT.messages.create( \
                    body = content, \
                    to = "+14048344779", \
                    from_= "+17209031234")
    except TwilioRestException as some_exception:
        print some_exception

SCHED = Scheduler()

HTML_QUIRKS = { \
"&amp;" : "&", "&quot;" : '"', "&apos;" : "'", "&gt;" : ">", "&lt;" : "<" \
}

@SCHED.cron_schedule(hour = 7)
def random_chuck_norris_generator():
    '''
    GET a random joke using ICNdB API. Send the retrieved joke to +14048344779.
    '''
    response = get('http://api.icndb.com/jokes/random')
    if response.json()['type'] == 'success':
        joke = str(response.json()[u'value'][u'joke'])
        for chars in HTML_QUIRKS:
            joke = joke.replace(chars, HTML_QUIRKS[chars])
        send_message('\n*****\n' + joke + '\n*****\n')

SCHED.start()

while True:
    pass

        
