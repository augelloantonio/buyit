import json
from django.utils.translation import get_language
from django.conf import settings

def get_available_languages():
    """
    Returns the available languages defined in the settings.
    """
    
    return settings.LANGUAGES


def load_translations():
    """
    Load actual language.
    """
    lang = get_language()  # Get the current language
        
    try:
        with open(f"static/locale/{lang}.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        # Fallback to default language
        with open("static/locale/en.json", "r") as f:
            return json.load(f)