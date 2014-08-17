## What?
*  [Chuck Norris dB](http://www.icndb.com/) + Heroku + Twilio

## Why?
*  Like 'Chuck Norris' jokes?
*  Would you like Heroku to serve you a new joke everyday?
*  Want to experiment with __Twilio__?

## How?
*  You'll have to setup a trial account on Twilio, [more details](https://www.twilio.com/help/faq/twilio-basics/how-does-twilios-free-trial-work).
*  Once you log into your account, you'll be able to retrieve **ACCOUNT_SID** and **AUTH_TOKEN**. Paste these values in source code as strings.
*  Also, through this account, you'll have to issue a *Free Trial Number*, and register the number to which you want your jokes to be sent to. You'll have to add **YOUR_NUMBER** (the number you want the SMS to be sent to) and **TWILIO_REGISTERED_NUM** (Free Trial Number) to source code as well (as strings).
*  The current setup SMSs jokes at 0700 hours, everyday. Should you want to change that, you can do so by changing the *hour* variable's value (line 33) from 7 to an integer between `0-23`, inclusive.
*  [If haven't deployed on Heroku before](https://devcenter.heroku.com/articles/getting-started-with-python).

