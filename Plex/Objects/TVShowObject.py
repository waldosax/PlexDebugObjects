from datetime import date
from MetadataObject import MetadataObject

class TVShowObject(MetadataObject):
    """Represents a TV show, or the top-level of other episodic content."""
    def __init__(self, **kwargs):
        super().__init__()
        self.key = str(kwargs.get("key"))
        """A string specifying the path to a container representing the show’s content. This is usually a function callback generated using Callback()."""
        
        self.rating_key = str(kwargs.get("rating_key"))
        """A string specifying a unique identifier for the show. This unique value is used by the media server for maintaining play counts and providing other advanced features."""
        
        self.genres = []
        """A list of attributes specifying the show’s genres."""
        if kwargs.get("genres"):
            for item in kwargs["genres"]:
                self.genres.append(str(item))
        
        self.tags = []
        """A list of attributes specifying the show’s tags."""
        if kwargs.get("tags"):
            for item in kwargs["tags"]:
                self.tags.append(str(item))
        
        self.rating = float(kwargs.get("rating") or 0.0)
        """A float between 0 and 10 specifying the show’s rating"""
        
        self.source_title = str(kwargs.get("source_title"))
        """A string specifying the source of the show (e.g. Netflix or YouTube)"""
        
        self.title = str(kwargs.get("title"))
        """A string specifying the show’s title."""
        
        self.summary = str(kwargs.get("summary"))
        """A string specifying the show’s summary."""
        
        self.originally_available_at = kwargs.get("originally_available_at") if isinstance(kwargs.get("originally_available_at"), date) else None
        """A date object specifying the date the show originally started airing,"""
        
        self.content_rating = str(kwargs.get("content_rating"))
        """A string specifying the show’s content rating."""
        
        self.studio = str(kwargs.get("studio"))
        """A string specifying the studio that produced the show."""
        
        self.countries = []
        """A list of strings specifying the countries involved in the production of the show."""
        if kwargs.get("countries"):
            for item in kwargs["countries"]:
                self.countries.append(str(item))
        
        self.thumb = str(kwargs.get("thumb"))
        """A string specifying an image resource to use as the show’s thumbnail."""
        
        self.art = str(kwargs.get("art"))
        """A string specifying an image resource to use as the show’s background art."""
        
        self.episode_count = int(kwargs.get("episode_count") or 0)
        """An integer specifying the TV show’s total number of episodes."""
        
        