import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """
    Translates the input text in English to French using IBM Watson Language Translator

    Parameters:
    englishText (str): The text in English to be translated to French

    Returns:
    str: The translated text in French
    """

    translation = language_translator.translate(
        text=english_text,
        source='en',
        target='fr'
    ).get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """
    Translates the input text in French to English using IBM Watson Language Translator

    Parameters:
    frenchText (str): The text in French to be translated to English

    Returns:
    str: The translated text in English
    """

    translation = language_translator.translate(
        text=french_text,
        source='fr',
        target='en'
    ).get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
