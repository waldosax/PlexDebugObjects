from datetime import date
from .MetadataObject import MetadataObject

class ArtistObject(MetadataObject):
    """Represents an artist or group."""
    def __init__(self, **kwargs):
        super().__init__()
        self.key = str(kwargs.get("key"))
        """A string specifying the path to a container representing the artist's content. This is usually a function callback generated using Callback()."""
        
        self.genres = []
        """A list of strings specifying the artist's genres."""
        if kwargs.get("genres"):
            for item in kwargs["genres"]:
                self.genres.append(str(item))
        
        self.tags = []
        """A list of strings specifying the artist's tags."""
        if kwargs.get("tags"):
            for item in kwargs["tags"]:
                self.tags.append(str(item))
        
        self.duration = int(kwargs.get("duration")) if kwargs.get("duration") else None
        """An integer specifying the total duration of the artist's albums, in milliseconds."""
        
        self.rating = float(kwargs.get("rating")) if kwargs.get("rating") else None
        """A float between 0 and 10 specifying the artist's rating."""
        
        self.source_title = str(kwargs.get("source_title"))
        """A string specifying the source of the artist (e.g. Rhapsody or Spotify)"""
        
        self.title = str(kwargs.get("title"))
        """A string specifying the artist's name."""
        
        self.summary = str(kwargs.get("summary"))
        """A string specifing the artist's biography."""
        
        self.thumb = str(kwargs.get("thumb"))
        """A string specifying an image resource to use as the artist's thumbnail."""
        
        self.art = str(kwargs.get("art"))
        """A string specifying an image resource to use as the artist's background art."""
        
        self.track_count = int(kwargs.get("track_count") or 0)
        """An integer specifying the total number of tracks available for the artist."""
        
        