**Mnotify Python Client**
- Mnotify is a simple Python client for sending SMS OTP (One Time Password) messages using the Mnotify API.

**Features**
- Send OTP messages via the Mnotify API.
- Easy to set up and use.

**Installation**
Clone the repository to your local machine:

```bash
`git clone https://github.com/adutwum-emma/mnotify-otp.git`
`cd mnotify-otp`
```

Ensure you have requests library installed. You can install it via pip:

```bash
`pip install requests`
```

**Usage**
-Initialization

```python
from mnotify import Mnotify

api_key = 'your_api_key_here'
mnotify = Mnotify(api_key=api_key)
```

**Sending an OTP SMS**

```python
recipient = 'recipient_phone_number'
sender = 'sender_id'
message = 'Your OTP code is 123456'

response = mnotify.sms_otp(recipient, sender, message)
print(response)
```

**Error Handling**
- If the API key is not provided, the sms_otp method will print an error message indicating that the API key is required.

**License**
- This project is not licensed any organization or standard authority.

**Contributing**
- Contributions are welcome! Please fork the repository and create a pull request with your changes.

**Contact**
- For any questions or issues, please open an issue in this repository or contact the maintainer at emmanuelkyeiadutwum@gmail.com.


