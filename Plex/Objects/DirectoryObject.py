from .GenericBrowsingObject import GenericBrowsingObject

class DirectoryObject(GenericBrowsingObject):
    """Represents a generic container of objects. Directory objects are usually used when creating a navigation hierarchy."""
    def __init__(self, **kwargs):
        super().__init__()
        self.key = str(kwargs.get("key"))
        """A string specifying the path to a container representing the directory’s content. This is usually a function callback generated using Callback()."""
        
        self.duration = int(kwargs.get("duration")) if kwargs.get("duration") else None
        """An integer specifying the duration of the objects provided by the directory, in milliseconds."""
        
        