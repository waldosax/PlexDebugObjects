from .MetadataModel import MetadataModel
from .Proxy import Proxy

class Episode(MetadataModel):
    """Represents an episode of a TV show or other episodic content."""
    def __init__(self, **kwargs):
        super().__init__()
        self.title = str(kwargs.get("title"))
        """A string specifying the episode's title."""
        
        self.summary = str(kwargs.get("summary"))
        """A string specifying the episode's summary."""
        
        self.originally_available_at = kwargs.get("originally_available_at") if isinstance(kwargs.get("originally_available_at"), date) else None
        """A date object specifying when the episode originally aired."""
        
        self.rating = int(kwargs.get("rating")) if kwargs.get("rating") else None
        """An integer attribute with a valuebetween 0 and 10 specifying the episode's rating."""
        
        self.writers = []
        """A set of strings specifying the episode's writers."""
        if kwargs.get("writers"):
            for item in kwargs["writers"]:
                self.writers.append(str(item))
        
        self.directors = []
        """A set of strings specifying the episode's directors."""
        if kwargs.get("directors"):
            for item in kwargs["directors"]:
                self.directors.append(str(item))
        
        self.producers = []
        """A set of strings specifying the episode's producers."""
        if kwargs.get("producers"):
            for item in kwargs["producers"]:
                self.producers.append(str(item))
        
        self.guest_stars = []
        """A set of strings specifying the episode's guest stars."""
        if kwargs.get("guest_stars"):
            for item in kwargs["guest_stars"]:
                self.guest_stars.append(str(item))
        
        self.absolute_index = int(kwargs.get("absolute_index") or 1)
        """An integer specifying the absolute index of the episode within the entire series."""
        
        self.thumbs = []
        """A container of proxy objects representing the episode's thumbnail images. See below for information about proxy objects."""
        if kwargs.get("thumbs"):
            for item in kwargs["thumbs"]:
                if (isinstance(item, Proxy)):
                    self.thumbs.append(item)
        
        self.duration = int(kwargs.get("duration")) if kwargs.get("duration") else None
        """An integer specifying the duration of the episode, in milliseconds."""
        
        