from datetime import date
from MetadataObject import MediaSupportingMetadataObject

class TrackObject(MediaSupportingMetadataObject):
    """Represents an audio track (e.g. music, audiobook, podcast, etc.)"""
    def __init__(self, **kwargs):
        super().__init__()
        self.url = str(kwargs.get("url"))
        """A string specifying the URL of the track. If a URL service that matches the given URL is available, the key and rating_key attributes will be set and the list of media objects will be generated automatically."""
        
        self.key = str(kwargs.get("key"))
        """A string specifying the path to the track’s full metadata object. This is usually a function callback generated using Callback(). The function should return an ObjectContainer containing a single metadata object with the maximum amount of metadata available.

Note

If the url attribute is set (invoking a URL service), the key attribute is set automatically."""
        
        self.title = str(kwargs.get("title"))
        """A string specifying the track’s title."""
        
        self.rating_key = str(kwargs.get("rating_key"))
        """A string specifying a unique identifier for the track. This unique value is used by the media server for maintaining play counts and providing other advanced features.

Note

If the url attribute is set (invoking a URL service), the rating_key attribute is set automatically."""
        
        self.index = int(kwargs.get("index") or 1)
        """An integer specifying the track’s index in the parent album."""
        
        self.artist = str(kwargs.get("artist"))
        """A string specifying the artist the track belongs to."""
        
        self.album = str(kwargs.get("album"))
        """A string specifying the album the track belongs to."""
        
        self.genres = []
        """A list of strings specifying the track’s genres."""
        if kwargs.get("genres"):
            for item in kwargs["genres"]:
                self.genres.append(str(item))
        
        self.tags = str(kwargs.get("tags"))
        """A list of strings specifying the track’s tags."""
        
        self.duration = int(kwargs.get("duration") or 0)
        """An integer specifying the duration of the track, in milliseconds."""
        
        self.rating = float(kwargs.get("rating")) if kwargs.get("rating") else None
        """A float between 0 and 10 specifying the track’s rating."""
        
        self.source_title = str(kwargs.get("source_title"))
        """A string specifying the source of the track (e.g. Rhapsody or Spotify)"""
        
        self.thumb = str(kwargs.get("thumb"))
        """A string specifying an image resource to use as the track’s thumbnail."""
        
        self.art = str(kwargs.get("art"))
        """A string specifying an image resource to use as the track’s background art."""
  
    
    def add(self, obj: MediaObject()):
        """Adds the MediaObject instance obj to the track’s item list. The items can also be populated by passing a list of objects to the constructor as the items argument:

obj = TrackObject(
   items = [
      MediaObject(...)
   ]
)"""
        super(self, obj)
       
        