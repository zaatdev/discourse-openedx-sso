

def plugin_settings(settings):
    """
    Injects local settings into django settings
    """
    settings.DISCOURSE_VALIDATE_EMAIL = False
    settings.DISCOURSE_SECRET = ''
