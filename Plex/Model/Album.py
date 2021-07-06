from datetime import date
from MetadataModel import MetadataModel
from Proxy import Proxy
from Track import Track

class Album(MetadataModel):
    """Represents a music album."""
    def __init__(self, **kwargs):
        super().__init__()
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
                
        self.collections = []
        """A list of strings specifying the collections the album belongs to."""
        if kwargs.get("collections"):
            for item in kwargs["collections"]:
                self.collections.append(str(item))
        
        self.rating = float(kwargs.get("rating")) if kwargs.get("rating") else None
        """A float between 0 and 10 specifying the album’s rating."""
        
        self.original_title = str(kwargs.get("original_title"))
        """A string specifying the album’s original title."""
        
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
        
        self.posters = []
        """A container of proxy objects representing the album’s covers. See below for information about proxy objects."""
        if kwargs.get("posters"):
            for item in kwargs["posters"]:
                if (isinstance(item, Proxy)):
                    self.posters.append(item)
        
        self.tracks = []
        """A map of Track objects representing the album’s tracks."""
        if kwargs.get("tracks"):
            for item in kwargs["tracks"]:
                if (isinstance(item, Track)):
                    self.tracks.append(item)
        
        


