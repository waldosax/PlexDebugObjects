from datetime import date
from .MetadataObject import MetadataObject

class AlbumObject(MetadataObject):
    """Represents a music album."""
    def __init__(self, **kwargs):
        super().__init__()
        self.key = str(kwargs.get("key"))
        """A string specifying the path to a container representing the album’s tracks. This is usually a function callback generated using Callback()."""
        
        self.genres = []
        """A list of strings specifying the album’s genres."""
        if kwargs.get("genres"):
            for item in kwargs["genres"]:
                self.genres.append(str(item))
        
        self.tags = []
        """A list of strings specifying the album’s tags."""
        if kwargs.get("tags"):
            for item in kwargs["tags"]:
                self.tags.append(str(item))
        
        self.duration = int(kwargs.get("duration")) if kwargs.get("duration") else None
        """An integer specifying the duration of the album, in milliseconds."""
        
        self.rating = float(kwargs.get("rating")) if kwargs.get("rating") else None
        """A float between 0 and 10 specifying the album’s rating."""
        
        self.original_title = str(kwargs.get("original_title"))
        """A string specifying the album’s original title."""
        
        self.source_title = str(kwargs.get("source_title"))
        """A string specifying the source of the album (e.g. Rhapsody or Spotify)"""
        
        self.artist = str(kwargs.get("artist"))
        """A string specifying the artist the album belongs to."""
        
        self.title = str(kwargs.get("title"))
        """A string specifying the album’s title."""
        
        self.summary = str(kwargs.get("summary"))
        """A string specifying the album’s summary."""
        
        self.studio = str(kwargs.get("studio"))
        """A string specifying the album’s studio."""
        
        self.originally_available_at = kwargs.get("originally_available_at") if isinstance(kwargs.get("originally_available_at"), date) else None
        """A date object specifying the album’s original release date."""
        
        self.producers = []
        """A list of strings specifying the album’s producers."""
        if kwargs.get("producers"):
            for item in kwargs["producers"]:
                self.producers.append(str(item))
        
        self.countries = []
        """A list of strings specifying the countries involved in the production of the album."""
        if kwargs.get("countries"):
            for item in kwargs["countries"]:
                self.countries.append(str(item))
        
        self.track_count = int(kwargs.get("track_count") or 0)
        """An integer value specifying the number of tracks the album contains."""
        
        self.thumb = str(kwargs.get("thumb"))
        """A string specifying an image resource to use as the album’s thumbnail."""
        
        self.art = str(kwargs.get("art"))
        """A string specifying an image resource to use as the album’s background art."""
        
        