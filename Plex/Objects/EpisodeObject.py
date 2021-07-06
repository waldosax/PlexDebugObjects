from datetime import date
from .MediaObject import MediaObject
from .MetadataObject import MediaSupportingMetadataObject

class EpisodeObject(MediaSupportingMetadataObject):
    """Represents an episode of a TV show or other episodic content."""
    def __init__(self, **kwargs):
        super().__init__()
        self.url = str(kwargs.get("url"))
        """A string specifying the URL of the movie. If a URL service that matches the given URL is available, the key and rating_key attributes will be set and the list of media objects will be generated automatically."""
        
        self.rating_key = str(kwargs.get("rating_key"))
        """A string specifying a unique identifier for the episode. This unique value is used by the media server for maintaining play counts and providing other advanced features.

Note

If the url attribute is set (invoking a URL service), the rating_key attribute is set automatically."""
        
        self.title = str(kwargs.get("title"))
        """A string specifying the episode’s title."""
        
        self.summary = str(kwargs.get("summary"))
        """A string specifying the episode’s summary."""
        
        self.orinally_available_at = kwargs.get("orinally_available_at") if isinstance(kwargs.get("orinally_available_at"), date) else None
        """A date object specifying when the episode originally aired."""
        
        self.rating = int(kwargs.get("rating") or 0)
        """An integer attribute with a valuebetween 0 and 10 specifying the episode’s rating."""
        
        self.writers = []
        """A list of strings specifying the episode’s writers."""
        if kwargs.get("writers"):
            for item in kwargs["writers"]:
                self.writers.append(str(item))
        
        self.directors = []
        """A list of strings specifying the episode’s directors."""
        if kwargs.get("directors"):
            for item in kwargs["directors"]:
                self.directors.append(str(item))
        
        self.producers = []
        """A list of strings specifying the episode’s producers."""
        if kwargs.get("producers"):
            for item in kwargs["producers"]:
                self.producers.append(str(item))
        
        self.guest_stars = []
        """A list of strings specifying the episode’s guest stars."""
        if kwargs.get("guest_stars"):
            for item in kwargs["guest_stars"]:
                self.guest_stars.append(str(item))
        
        self.abosolute_index = int(kwargs.get("abosolute_index") or 1)
        """An integer specifying the absolute index of the episode within the entire series."""
        
        self.key = str(kwargs.get("key"))
        """A string specifying the path to the episode’s full metadata object. This is usually a function callback generated using Callback(). The function should return an ObjectContainer containing a single metadata object with the maximum amount of metadata available.

Note

If the url attribute is set (invoking a URL service), the key attribute is set automatically."""
        
        self.show = str(kwargs.get("show"))
        """A string identifying the show the episode belongs to."""
        
        self.season = int(kwargs.get("season") or 0)
        """An integer identifying the season the episode belongs to."""
        
        self.thumb = str(kwargs.get("thumb"))
        """A string specifying an image resource to use as the episode’s thumbnail."""
        
        self.art = str(kwargs.get("art"))
        """A string specifying an image resource to use as the episode’s background art."""
        
        self.source_title = str(kwargs.get("source_title"))
        """A string specifying the source of the episode (e.g. Netflix or YouTube)"""
        
        self.duration = int(kwargs.get("duration") or 0)
        """An integer specifying the duration of the episode, in milliseconds."""
 
    
    def add(self, obj: MediaObject()):
        """Adds the MediaObject instance obj to the episode's item list. The items can also be populated by passing a list of objects to the constructor as the items argument:

m = EpisodeObject(
   items = [
      MediaObject(...)
   ]
)"""
        super(self, obj)       


# episode = EpisodeObject(items=[MediaObject(), MediaObject()])
# print(len(episode.items))