#!/usr/bin/python

from twilio.rest import TwilioRestClient
from twilio import TwilioRestException
from apscheduler.scheduler import Scheduler
from requests import get

ACCOUNT_SID = <ACCNT_SID>
AUTH_TOKEN = <AUTH_TOK>
YOUR_NUMBER = <NUM1>
TWILIO_REGISTERED_NUM = <NUM2>

CLIENT = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

def send_message(content):
    '''
    Wrapper function which calls Twilio API
    '''
    try:
        CLIENT.messages.create( \
                    body = content, \
                    to = YOUR_NUMBER, \
                    from_= TWILIO_REGISTERED_NUM)
    except TwilioRestException as some_exception:
        print some_exception

SCHED = Scheduler()

HTML_QUIRKS = { \
"&amp;" : "&", "&quot;" : '"', "&apos;" : "'", "&gt;" : ">", "&lt;" : "<" \
}

@SCHED.cron_schedule(hour = 7)
def random_chuck_norris_generator():
    '''
    GET a random joke using ICNdB API. Send the retrieved joke to YOUR_NUMBER.
    '''
    response = get('http://api.icndb.com/jokes/random').json()
    if response['type'] == 'success':
        joke = str(response[u'value'][u'joke'])
        for chars in HTML_QUIRKS:
            joke = joke.replace(chars, HTML_QUIRKS[chars])
        send_message('\n*****\n' + joke + '\n*****\n')

SCHED.start()

while True:
    pass

        
