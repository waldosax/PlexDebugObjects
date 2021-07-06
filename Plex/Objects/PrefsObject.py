from .GenericBrowsingObject import GenericBrowsingObject

class PrefsObject(GenericBrowsingObject):
    """Represents an item that invokes the user preferences dialog when selected."""
    def __init__(self, **kwargs):
        super().__init__()
