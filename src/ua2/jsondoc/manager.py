from __future__ import unicode_literals

from importlib import import_module

from django.core.urlresolvers import reverse
from .encoder import JsonDocEncoder


class JsonBaseManager(object):
    def __init__(self, json_data):
        self.json_data = json_data

    def get_instance(self, data):
        _module = import_module(data['module'])
        cls = getattr(_module, data['model'])
        return cls.objects.get(pk=data['id'])

    def _label(self, data):
        return data.get('label', None)

    def _url(self, data):
        return reverse(data['url']['url_name'],
                       kwargs=data['url']['url_parametres'])

    def short_description(self):
        raise NotImplementedError

    def url(self):
        raise NotImplementedError

    def description(self):
        raise NotImplementedError


class JsonObjectManager(JsonBaseManager):
    def url(self):
        return self._url(self.json_data)

    def short_description(self):
        return self.label(self.json_data)

    def description(self):
        return [self.label(self.json_data)]

    @property
    def instance(self):
        return self.get_instance(self.json_data)


class JsonListManager(JsonBaseManager):
    def __iter__(self):
        for item in self.json_data:
            yield self.get_instance(item)

    def __getitem__(self, key):
        if hasattr(self, key) and callable(getattr(self, key)):
            return getattr(self, key)

        for item in self.json_data:
            if item.get('model', '') == key:
                return self.get_instance(item)
        return None

    def append(self, instance):
        self.json_data.append(JsonDocEncoder(instance).dump())

    def label(self):
        for item in self.json_data:
            label = self._label(item)
            if label is not None:
                return label
        return None

    def url(self):
        for item in self.json_data:
            if 'url' in item:
                return self._url(item)
        return None

    def description(self):
        rc = []
        for item in self.json_data:
            label = self.label(item)
            if label:
                rc.append(label)
        return ", ".join(rc)


class JsonDocManager(JsonListManager):
    def __init__(self, json_data):
        raise DeprecationWarning("JsonDocManager deprecated, please use JsonListManager instead")
        super(JsonDocManager, self).__init__(json_data)
