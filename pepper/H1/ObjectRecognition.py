import requests
import os
import sys

class ObjectRecognition:
    """
    Use this class to query Azure ObjectRecognition
    The specified file path is defined below
    """
    def __init__(self):
        if 'COMPUTER_VISION_SUBSCRIPTION_KEY' in os.environ:
            self.subscription_key = os.environ['COMPUTER_VISION_SUBSCRIPTION_KEY']
        else:
            print(
                "\nSet the COMPUTER_VISION_SUBSCRIPTION_KEY environment variable.\n**Restart your shell or IDE for changes to take effect.**")
            sys.exit()

        if 'COMPUTER_VISION_ENDPOINT' in os.environ:
            self.endpoint = os.environ['COMPUTER_VISION_ENDPOINT']

        self.analyze_url = self.endpoint + "vision/v3.1/analyze"
        self.image_path = "C:\work\latest.jpg"
        self.image_data = open(self.image_path, "rb").read()
        self.headers = {'Ocp-Apim-Subscription-Key': self.subscription_key,
                   'Content-Type': 'application/octet-stream'}
        self.params = {'visualFeatures': 'Categories,Description,Color'}
        self.response = requests.post(
            self.analyze_url, headers=self.headers, params=self.params, data=self.image_data)
        self.response.raise_for_status()
        self.jsonresponse = self.response.json()

    def getTags(self):
        return self.jsonresponse['description'].get('tags')

    def getTagsEncoded(self):
        data = self.jsonresponse['description'].get('tags')
        data = str(data)
        data = data.encode()
        return data

    def getFullResponse(self):
        return self.jsonresponse


if __name__ == "__main__":
    or1 = ObjectRecognition()
    print(or1.getTags())
    print(or1.getTagsEncoded())
    print(or1.getFullResponse())