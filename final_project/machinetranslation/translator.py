"""System"""
from deep_translator import MyMemoryTranslator

def englishtofrench(text):
    """
    Translator from English to French
    """
    translator = MyMemoryTranslator(source='english', target='french').translate(text)
    return translator

def frenchtoenglish(text):
    """
    Translator from French to English
    """
    translator = MyMemoryTranslator(source='french', target='english').translate(text)
    return translator
