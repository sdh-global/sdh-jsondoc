class JsonDocEncoder(object):
    def __init__(self, data_object):
        self.data_object = data_object

    def key(self):
        return {
            'id': self.data_object.id,
            'module': self.data_object.__class__.__module__,
            'model': self.data_object.__class__.__name__}

    def dump(self):
        data = self.key()
        data['title'] = unicode(self.data_object)
        return data
