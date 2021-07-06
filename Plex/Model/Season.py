from Episode import Episode
from MetadataModel import MetadataModel
from Proxy import Proxy

class Season(MetadataModel):
    """Represents a season of a TV show."""
    def __init__(self, **kwargs):
        super().__init__()
        self.summary = str(kwargs.get("summary"))
        """A string specifying the season’s summary."""
        
        self.posters = []
        """A container of proxy objects representing the season’s posters. See below for information about proxy objects."""
        if kwargs.get("posters"):
            for item in kwargs["posters"]:
                if (isinstance(item, Proxy)):
                    self.posters.append(item)
        
        self.banners = []
        """A container of proxy objects representing the season’s banner images. See below for information about proxy objects."""
        if kwargs.get("banners"):
            for item in kwargs["banners"]:
                if (isinstance(item, Proxy)):
                    self.banners.append(item)
        
        self.episodes = []
        """A map of Episode objects."""
        if kwargs.get("episodes"):
            for item in kwargs["episodes"]:
                if (isinstance(item, Episode)):
                    self.episodes.append(item)
        
        