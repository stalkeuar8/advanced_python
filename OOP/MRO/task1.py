

class BasePaymentConnector:

    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key

    def _send_request(self, endpoint):
        print(f"Sending to {self.base_url}/{endpoint} with key {self.api_key}")

class StripeConnector(BasePaymentConnector):

    def __init__(self, api_key):
        super().__init__(base_url='https://api.stripe.com', api_key=api_key)


class PayPalConnector(BasePaymentConnector):

    def __init__(self, api_key):
        super().__init__(base_url="https://api.paypal.com", api_key=api_key)


        