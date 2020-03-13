import requests


class BlockChainFetchInfo:

    def __init__(self):
        self.api_code = '8a84bc08-438d-4faa-a2ba-dfb1909bf837'
        self.base_url = 'https://blockchain.info'

    def get_api_code(self):
        return self.api_code

    def exchangeRates(self, coin='*'):
        url = '%s/ticker' % self.base_url

        response = requests.get(url)
        response_json = response.json()

        if coin is not '*':
            return response_json[coin]

        return response_json

    def amountInBTC(self, coin='USD', amount=1):
        url = '%s/tobtc?currency=%s&value=%s' % (self.base_url, coin, amount)

        response = requests.get(url)
        response_json = response.json()

        return response_json
