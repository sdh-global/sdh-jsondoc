from .encoder import JsonDocEncoder

class JsonDocManager(object):
    def __init__(self, json_data):
        self.json_data = json_data

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

    def get_instance(self, data):
        _module = import_module(data['module'])
        cls = getattr(_module, data['model'])
        return cls.objects.get(pk=data['id'])

    def append(self, instance):
        self.json_data.append(JsonDocEncoder(instance).dump())

    def short_description(self):
        for item in self.json_data:
            if 'title' in item:
                return item['title']
        return None

    def description(self):
        rc = []
        for item in self.json_data:
            if 'title' in item:
                rc.append(item['title'])
        return rc
