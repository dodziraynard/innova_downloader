from django.apps import AppConfig


class WebsiteConfig(AppConfig):
    name = 'website'

    def ready(self):
        from . import signals
