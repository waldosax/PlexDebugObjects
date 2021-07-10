from .MetadataModel import MetadataModel
from .Proxy import Proxy

class TV_Show(MetadataModel):
    """Represents a TV show, or the top-level of other episodic content."""
    def __init__(self, **kwargs):
        super().__init__()
        self.genres = []
        """A set of strings specifying the show's genres."""
        if kwargs.get("genres"):
            for item in kwargs["genres"]:
                self.genres.append(str(item))
        
        self.tags = []
        """A set of strings specifying the show's tags."""
        if kwargs.get("tags"):
            for item in kwargs["tags"]:
                self.tags.append(str(item))
        
        self.collections = []
        """A set of strings specifying the show's collections."""
        if kwargs.get("collections"):
            for item in kwargs["collections"]:
                self.collections.append(str(item))
        
        self.duration = int(kwargs.get("duration")) if kwargs.get("duration") else None
        """An integer specifying the approximate duration of each episode in the show, in milliseconds."""
        
        self.rating = float(kwargs.get("rating")) if kwargs.get("rating") else None
        """A float between 0 and 10 specifying the show's rating."""
        
        self.title = str(kwargs.get("title"))
        """A string specifying the show's title."""
        
        self.summary = str(kwargs.get("summary"))
        """A string specifying the show's summary."""
        
        self.originally_available_at = kwargs.get("originally_available_at") if isinstance(kwargs.get("originally_available_at"), date) else None
        """A date object specifying the date the show originally started airing,"""
        
        self.content_rating = str(kwargs.get("content_rating"))
        """A string specifying the show's content rating."""
        
        self.studio = str(kwargs.get("studio"))
        """A string specifying the studio that produced the show."""
        
        self.countries = []
        """A set of strings specifying the countries involved in the production of the show."""
        if kwargs.get("countries"):
            for item in kwargs["countries"]:
                self.countries.append(str(item))
        
        self.posters = []
        """A container of proxy objects representing the show's posters. See below for information about proxy objects."""
        if kwargs.get("posters"):
            for item in kwargs["posters"]:
                if (isinstance(item, Proxy)):
                    self.posters.append(item)
        
        self.banners = []
        """A container of proxy objects representing the show's banner images. See below for information about proxy objects."""
        if kwargs.get("banners"):
            for item in kwargs["banners"]:
                if (isinstance(item, Proxy)):
                    self.banners.append(item)
        
        self.art = []
        """A container of proxy objects representing the show's banner images. See below for information about proxy objects."""
        if kwargs.get("art"):
            for item in kwargs["art"]:
                if (isinstance(item, Proxy)):
                    self.art.append(item)
        
        self.themea = []
        """A container of proxy objects representing the show's theme music. See below for information about proxy objects."""
        if kwargs.get("themea"):
            for item in kwargs["themea"]:
                if (isinstance(item, Proxy)):
                    self.themea.append(item)
        
        