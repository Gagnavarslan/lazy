#coding: utf-8
from importlib import import_class
from lazy_object import LazyObject
import os


class BaseLazyImplementation(LazyObject):
    DEFAULT = None
    ImproperlyConfigured = Exception

    def _setup(self):
        class_name = self._get_class_name()
        impl_class = import_class(class_name)
        self._wrapped = impl_class(*self._args, **self._kwargs)


class LazyEnvironImplementation(BaseLazyImplementation):
    ENV_KEY = None

    def _get_class_name(self):
        if self.ENV_KEY is None:
            raise self.ImproperlyConfigured("ENV_KEY for '%s' is undefined"
                                            % self.__class__.__name__)

        if not self.ENV_KEY in os.environ:
            if not self.DEFAULT:
                raise self.ImproperlyConfigured("No environment param '%s'"
                                                % self.ENV_KEY)
            class_name = self.DEFAULT
        else:
            class_name = os.environ[self.ENV_KEY]

        return class_name


class LazySettingImplementation(BaseLazyImplementation):
    SETTING_NAME = None
    settings = None

    def _get_class_name(self):
        if self.settings is None:
            raise self.ImproperlyConfigured("No settings defined for '%s'"
                                            % self.__class__.__name__)

        if self.SETTING_NAME is None:
            raise self.ImproperlyConfigured("SETTING_NAME for '%s' is undefined"
                                            % self.__class__.__name__)

        if not hasattr(self.settings, self.SETTING_NAME):
            if not self.DEFAULT:
                raise self.ImproperlyConfigured("No setting '%s'"
                                                % self.SETTING_NAME)
            class_name = self.DEFAULT
        else:
            class_name = getattr(self.settings, self.SETTING_NAME)

        return class_name
