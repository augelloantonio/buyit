from utils.languageUtils import get_available_languages

def available_languages(request):
    """
    Adds available languages to the template context.
    """
    return {"LANGUAGES": get_available_languages()}