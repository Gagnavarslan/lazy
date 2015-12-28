#coding: utf-8
from lazy.importlib import import_module
from lazy.lazy_object import LazyObject
import os


class Settings(object):
    default_settings = None

    def __init__(self, settings_module=None, settings_module_name=None,
                 default_settings_module_name=None):

        if default_settings_module_name:
            default_settings_module = self._import_module(default_settings_module_name)
            self._set_settings_from_module(default_settings_module)

        if not settings_module:
            settings_module = self._import_module(settings_module_name)

        self._set_settings_from_module(settings_module)

    def _set_settings_from_module(self, mod):
        for setting in dir(mod):
            if setting == setting.upper():
                setattr(self, setting, getattr(mod, setting))

    def _import_module(self, module_name):
        try:
            return import_module(module_name)
        except ImportError, e:
            raise ImportError("Could not import settings '%s' "
                              "(Is it on sys.path? Does it have syntax errors?)"
                              ": %s" % (module_name, e))


class LazySettings(LazyObject):
    ENVIRONMENT_VARIABLE = None
    DEFAULT_SETTINGS_MODULE = None
    SETTINGS_CLS = Settings

    def _setup(self):
        try:
            settings_module_name = os.environ[self.ENVIRONMENT_VARIABLE]
            if not settings_module_name:  # If it's set but is an empty string.
                raise KeyError
        except KeyError:
            raise ImportError("Settings cannot be imported, because environment"
                              "variable %s is undefined." % self.ENVIRONMENT_VARIABLE)

        self._wrapped = self.SETTINGS_CLS(settings_module_name=settings_module_name,
                                          default_settings_module_name=self.DEFAULT_SETTINGS_MODULE)
