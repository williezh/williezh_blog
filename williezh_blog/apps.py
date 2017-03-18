from importlib import import_module

from django.apps import AppConfig as BaseAppConfig


class AppConfig(BaseAppConfig):

    name = "williezh_blog"

    def ready(self):
        import_module("williezh_blog.receivers")
