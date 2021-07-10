from .MetadataModel import MetadataModel
from .Proxy import Proxy

class Track(MetadataModel):
    """Represents an audio track (e.g. music, audiobook, podcast, etc.)"""
    def __init__(self, **kwargs):
        super().__init__()
        self.name = str(kwargs.get("name"))
        """A string specifying the track's name."""
        
        