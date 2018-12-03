from .credentials import google_apikey
import requests


def translate(texts):
    url = "https://translation.googleapis.com/language/translate/v2"
    headers = {'X-Goog-Api-Key': google_apikey, }
    data = {'q': texts, 'target': 'en', }
    json = requests.post(url, data=data, headers=headers).json()
    translated_texts = [x['translatedText']
                        for x in json['data']['translations']]
    return translated_texts


if __name__ == '__main__':
    print(translate(['こんにちは', '東京']))
