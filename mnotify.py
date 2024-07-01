import requests

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

mapi = Mnotify(api_key='j5USmsBoXbnEQ5dAOhoWB0JdWM9OC86Ve1NAupYrAm6rs')

print(mapi.sms_otp(reciepient='0559334838', sender='toskybrown', message='This is your OTP: 131'))