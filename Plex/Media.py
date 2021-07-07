from .Objects.MetadataObject import MetadataObject

class Media:
    """The media object provided to the search method provides the developer with all the hints found by the media server while scanning for media. For media that contains several individual playable items (e.g. albums or TV shows), the hints for the most recent item are provided."""
    def __init__(self, **kwargs):
        self.primary_metadata = kwargs.get("primary_metadata") if isinstance(kwargs.get("primary_metadata"), MetadataObject) else None
        """If the search is being called in a secondary agent, the metadata object from the primary agent will be provided here. If the search is being called in a primary agent, this attribute will be None."""

        self.primary_agent = str(kwargs.get("primary_agent"))
        """If the search is being called in a secondary agent, the identifier of the primary agent will be provided here. If the search is being called in a primary agent, this attribute will be None."""
        
        self.filename = str(kwargs.get("filename"))
        """The name of the media file on disk."""
        
        self.name = str(kwargs.get("name"))
        """A string identifying the name of the item, extracted from its’ filename or embedded metadata.
Note

This attribute is only available for Movie and TV Show metadata searches."""
        
        self.openSubtitlesHash = str(kwargs.get("openSubtitlesHash"))
        """A string identifying the hash of the file, as used by OpenSubtitles.org.

Note

This attribute is only available for Movie and TV Show metadata searches."""
        
        self.year = int(kwargs.get("year")) if kwargs.get("year") else None
        """The year associated with the item, extracted from its’ filename or embedded metadata.

Note

This attribute is only available for Movie and TV Show metadata searches."""
        
        self.duration = int(kwargs.get("duration")) if kwargs.get("duration") else None
        """The duration of the media, extracted from the video file.

Note

This attribute is only available for Movie and TV Show metadata searches."""
        
        self.show = str(kwargs.get("show"))
        """The name of the show the episode belongs to.

Note

This attribute is only available for TV Show metadata searches."""
        
        self.season = int(kwargs.get("season")) if kwargs.get("season") else None
        """The season of the show the episode belongs to.

Note

This attribute is only available for TV Show metadata searches."""
        
        self.episode = int(kwargs.get("episode")) if kwargs.get("episode") else None
        """The episode number.

Note

This attribute is only available for TV Show metadata searches."""
        
        self.artist = str(kwargs.get("artist"))
        """The name of the artist.

Note

This attribute is only available for Artist and Album metadata searches."""
        
        self.album = str(kwargs.get("album"))
        """The name of the album.

Note

This attribute is only available for Artist and Album metadata searches."""
        
        self.track = str(kwargs.get("track"))
        """The name of the track.

Note

This attribute is only available for Artist and Album metadata searches."""
        
        self.index = int(kwargs.get("index")) if kwargs.get("index") else None
        """The position of the track in the album.

Note

This attribute is only available for Album metadata searches."""
        
        self.parts = []
        """"""
        if kwargs.get("parts"):
            for item in kwargs["parts"]:
                if (isinstance(item, MediaPart)):
                    self.parts.append(item)
        
        self.items = []
        """"""
        if kwargs.get("items"):
            for item in kwargs["items"]:
                if (isinstance(item, Media)):
                    self.items.append(item)
        
        