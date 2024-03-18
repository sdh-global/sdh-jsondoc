try:
    from django.utils.encoding import force_text
except:
    from django.utils.encoding import force_str as force_text


class JsonDocEncoder:
    def __init__(self, data_object):
        self.data_object = data_object

    def key(self):
        return {
            'id': self.data_object.id,
            'module': self.data_object.__class__.__module__,
            'model': self.data_object.__class__.__name__}

    def dump(self):
        data = self.key()
        data['label'] = getattr(self.data_object, 'label', force_text(self.data_object))

        if hasattr(self.data_object, 'json_dump'):
            data.update(self.data_object.json_dump())

        return data
