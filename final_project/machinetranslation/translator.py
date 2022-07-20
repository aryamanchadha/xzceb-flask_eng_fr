import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
lt = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)
lt.set_service_url(url)

def english_to_french(englishText):
    """english to french translation"""
    translation = lt.translate(englishText, model_id='en-fr').get_result()
    frenchText = translation['translations'][0]['translation']
    return frenchText

def french_to_english(frenchText):
    """French to English Translation"""
    fTranslation = lt.translate(frenchText, model_id='fr-en').get_result()
    englishText = fTranslation['translations'][0]['translation']
    return englishText