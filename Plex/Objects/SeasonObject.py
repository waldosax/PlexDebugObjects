from .MetadataObject import MetadataObject

class SeasonObject(MetadataObject):
    """Represents a season of a TV show."""
    def __init__(self, **kwargs):
        super().__init__()
        self.summary = str(kwargs.get("summary"))
        """A string specifying the season’s summary."""
        
        self.key = str(kwargs.get("key"))
        """A string specifying the path to a container representing the season’s content. This is usually a function callback generated using Callback()."""
        
        self.rating_key = str(kwargs.get("rating_key"))
        """A string specifying a unique identifier for the season. This unique value is used by the media server for maintaining play counts and providing other advanced features."""
        
        self.index = int(kwargs.get("index") or 0)
        """An integer specifying the season’s index."""
        
        self.title = str(kwargs.get("title"))
        """A string specifying the title to display for the season in the user interface."""
        
        self.show = str(kwargs.get("show"))
        """A string specifying the show the season belongs to."""
        
        self.episoce_count = int(kwargs.get("episoce_count") or 0)
        """An integer specifying the number of episodes in the season."""
        
        self.source_title = str(kwargs.get("source_title"))
        """A string specifying the source of the season (e.g. Netflix or YouTube)"""
        
        self.thumb = str(kwargs.get("thumb"))
        """A string specifying an image resource to use as the season’s thumbnail."""
        
        self.art = str(kwargs.get("art"))
        """A string specifying an image resource to use as the season’s background art."""
        
        