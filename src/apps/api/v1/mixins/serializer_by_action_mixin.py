class SerializerByActionMixin:
    serializer_class_by_action = {}

    def get_serializer_class(self):
        if self.action in self.serializer_class_by_action:
            return self.serializer_class_by_action[self.action]
        return self.serializer_class
