from MetadataObject import MetadataObject

class GenericBrowsingObject(MetadataObject):
    """Base class for all generic browsing objects."""
    def __init__(self, **kwargs):
        self.title = str(kwargs.get("title"))
        """A string specifying the object’s title."""
        
        self.tagline = str(kwargs.get("tagline"))
        """A string specifying the object’s tagline."""
        
        self.summary = str(kwargs.get("summary"))
        """A string specifying the object’s summary."""
        
        self.thumb = str(kwargs.get("thumb"))
        """A string specifying an image resource to use as the object’s thumbnail."""
        
        self.art = str(kwargs.get("art"))
        """A string specifying an image resource to use as the object’s background art."""
        
        