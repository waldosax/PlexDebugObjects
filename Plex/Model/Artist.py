from .MetadataModel import MetadataModel
from .Proxy import Proxy

class Artist(MetadataModel):
    """Represents an artist or group."""
    def __init__(self, **kwargs):
        super().__init__()
        self.genres = []
        """A set of strings specifying the artist's genres."""
        if kwargs.get("genres"):
            for item in kwargs["genres"]:
                self.genres.append(str(item))
        
        self.tags = []
        """A set of strings specifying the artist's tags."""
        if kwargs.get("tags"):
            for item in kwargs["tags"]:
                self.tags.append(str(item))
        
        self.collections = []
        """A set of strings specifying the collections the artist belongs to."""
        if kwargs.get("collections"):
            for item in kwargs["collections"]:
                self.collections.append(str(item))
        
        self.rating = float(kwargs.get("rating")) if kwargs.get("rating") else None
        """A float between 0 and 10 specifying the artist's rating."""
        
        self.title = str(kwargs.get("title"))
        """A string specifying the artist's name."""
        
        self.summary = str(kwargs.get("summary"))
        """A string specifying the artist's biography."""
        
        self.posters = []
        """A container of proxy objects representing the artist's posters. See below for information about proxy objects."""
        if kwargs.get("posters"):
            for item in kwargs["posters"]:
                if (isinstance(item, Proxy)):
                    self.posters.append(item)
        
        self.art = []
        """A container of proxy objects representing the artist's background art. See below for information about proxy objects."""
        if kwargs.get("art"):
            for item in kwargs["art"]:
                if (isinstance(item, Proxy)):
                    self.art.append(item)
        
        self.themes = []
        """A container of proxy objects representing the artist's theme music. See below for information about proxy objects."""
        if kwargs.get("themes"):
            for item in kwargs["themes"]:
                if (isinstance(item, Proxy)):
                    self.themes.append(item)
        
        