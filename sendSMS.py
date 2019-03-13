# works with both python 2 and 3
from __future__ import print_function

import africastalking
import secret


class SMS:
    def __init__(self):
        # Set your app credentials
        self.username = secret.AT_USERNAME

        self.api_key = secret.AT_API_KEY

        # Initialize the SDK
        africastalking.initialize(self.username, self.api_key)

        # Get the SMS service
        self.sms = africastalking.SMS

    def send(self):
        # Set the numbers you want to send to in international format
        # recipients = ["+254799417969", "+254733YYYZZZ"]
        # recipients = ["+254799417969"]
        recipients = ["+254790152469"]

        # Set your message
        message = "Hello, you were recently visited by a CHV (nyamrerwa). Please dial *384*888# to provide " \
                  "feedback about the visit. This service is free. Thank you."

        # Set your shortCode or senderId
        sender = "CHV_Feedbk"
        try:
            response = self.sms.send(message, recipients, sender)
            # response = self.sms.send(message, recipients)
            print(response)
        except Exception as e:
            print('Encountered an error while sending: %s' % str(e))


if __name__ == '__main__':
    SMS().send()
