"""
madrasafree_services Django application initialization.
"""
# Check this for an example of using edx django plugin
# https://github.com/openedx/edx-bulk-grades/blob/master/bulk_grades/apps.py
from django.apps import AppConfig


class DiscourseOpenedxSSO(AppConfig):
#Configuration for the madrasafree_services Django application.


    name = 'discourse_openedx_sso'
    plugin_app = {
        'url_config': {
             'lms.djangoapp': {
                 'namespace': 'discourse_openedx_sso',
                 'regex': '^discourse/',
                 'relative_path': 'urls',
             },
        },
        'settings_config': {
            'lms.djangoapp': {
                'common': { 'relative_path': 'settings.common' },
            }
        },

    }
