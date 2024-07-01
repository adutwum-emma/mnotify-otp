import requests
import os

class Mnotify:

    def __init__(self, api_key=None) -> None:
        self.api = api_key
        self.end_point = 'https://api.mnotify.com/api/sms/otp'


    def sms_otp(self, reciepient, sender, message):

        if self.api is None:
            print('API key is required')
        else:

            data = {
                'recipient': reciepient,
                'sender': sender,
                'message':message,
            }
        
            url = f'{self.end_point}?key={self.api}'

            response = requests.post(url, data)

            return response.json()