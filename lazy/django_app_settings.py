#coding: utf-8
from django.conf import settings as django_settings
from lazy.lazy_object import LazyObject
from lazy.settings import Settings


class DjangoAppLazySettings(LazyObject):
    DEFAULT_SETTINGS_MODULE = None

    def _setup(self):
        self._wrapped = Settings(settings_module=django_settings,
                                 default_settings_module_name=self.DEFAULT_SETTINGS_MODULE)
