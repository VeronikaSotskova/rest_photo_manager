class PermissionsByActionMixin:
    permissions_by_action = {}
    permission_classes = []

    def get_permissions(self):
        if self.action in self.permissions_by_action:
            return [permission() for permission in self.permissions_by_action[self.action]]
        return [permission() for permission in self.permission_classes]
