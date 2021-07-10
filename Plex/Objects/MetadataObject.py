from .MediaObject import MediaObject

class MetadataObject:
    """Base class for all metadata objects."""
    def __init__(self, **kwargs):
        pass


class MediaSupportingMetadataObject:
    """Base class for all media-supporting (file) metadata objects."""
    def __init__(self, **kwargs):
        super().__init__()
        self.items = []
        if kwargs.get("items"):
            for item in kwargs["items"]:
                if (isinstance(item, MediaObject)):
                    self.items.append(item)


    def add(self, obj):
        if (isinstance(obj, MediaObject)):
            self.items.append(obj)
