from datetime import date
from MediaObject import MediaObject
from MetadataObject import MediaSupportingMetadataObject

class MovieObject(MediaSupportingMetadataObject):
    """Represents a movie (e.g. a theatrical release, independent film, home movie, etc.)"""
    def __init__(self, **kwargs):
        super().__init__()
        self.url = str(kwargs.get("url"))
        """A string specifying the URL of the movie. If a URL service that matches the given URL is available, the key and rating_key attributes will be set and the list of media objects will be generated automatically."""
        
        self.key = str(kwargs.get("key"))
        """A string specifying the path to the movie’s full metadata object. This is usually a function callback generated using Callback(). The function should return an ObjectContainer containing a single metadata object with the maximum amount of metadata available.

Note

If the url attribute is set (invoking a URL service), the key attribute is set automatically."""
        
        self.rating_key = str(kwargs.get("rating_key"))
        """A string specifying a unique identifier for the movie. This unique value is used by the media server for maintaining play counts and providing other advanced features.

Note

If the url attribute is set (invoking a URL service), the rating_key attribute is set automatically."""
        
        self.genres = []
        """A list of strings specifying the movie’s genre."""
        if kwargs.get("genres"):
            for item in kwargs["genres"]:
                self.genres.append(str(item))
        
        self.tags = []
        """A list of strings specifying the movie’s tags."""
        if kwargs.get("tags"):
            for item in kwargs["tags"]:
                self.tags.append(str(item))
        
        self.duration = int(kwargs.get("duration") or 0)
        """An integer specifying the duration of the movie, in milliseconds."""
        
        self.rating = float(kwargs.get("rating") or 0.0)
        """A float between 0 and 10 specifying the movie’s rating."""
        
        self.original_title = str(kwargs.get("original_title"))
        """A string specifying the movie’s original title."""
        
        self.source_title = str(kwargs.get("source_title"))
        """A string specifying the source of the movie (e.g. Netflix or YouTube)"""
        
        self.title = str(kwargs.get("title"))
        """A string specifying the movie’s title."""
        
        self.year = int(kwargs.get("year")) if kwargs.get("year") else None
        """An integer specifying the movie’s release year."""
        
        self.originally_available_at = kwargs.get("originally_available_at") if isinstance(kwargs.get("originally_available_at"), date) else None
        """A date object specifying the movie’s original release date."""
        
        self.studio = str(kwargs.get("studio"))
        """A string specifying the movie’s studio."""
        
        self.tagline = str(kwargs.get("tagline"))
        """A string specifying the movie’s tagline."""
        
        self.summary = str(kwargs.get("summary"))
        """A string specifying the movie’s summary."""
        
        self.trivia = str(kwargs.get("trivia"))
        """A string containing trivia about the movie."""
        
        self.quotes = str(kwargs.get("quotes"))
        """A string containing memorable quotes from the movie."""
        
        self.content_rating = str(kwargs.get("content_rating"))
        """A string specifying the movie’s content rating."""
        
        self.content_rating_age = str(kwargs.get("content_rating_age"))
        """A string specifying the minumum age for viewers of the movie."""
        
        self.writers = []
        """A list of strings specifying the movie’s writers."""
        if kwargs.get("writers"):
            for item in kwargs["writers"]:
                self.writers.append(str(item))
        
        self.directors = []
        """A list of strings specifying the movie’s directors."""
        if kwargs.get("directors"):
            for item in kwargs["directors"]:
                self.directors.append(str(item))
        
        self.producers = []
        """A list of strings specifying the movie’s producers."""
        if kwargs.get("producers"):
            for item in kwargs["producers"]:
                self.producers.append(str(item))
        
        self.countries = []
        """A list of strings specifying the countries involved in the production of the movie."""
        if kwargs.get("countries"):
            for item in kwargs["countries"]:
                self.countries.append(str(item))
        
        self.thumb = str(kwargs.get("thumb"))
        """A string specifying an image resource to use as the movie’s thumbnail."""
        
        self.art = str(kwargs.get("art"))
        """A string specifying an image resource to use as the movie’s background art."""

    
    def add(self, obj: MediaObject()):
        """Adds the MediaObject instance obj to the movie’s item list. The items can also be populated by passing a list of objects to the constructor as the items argument:

m = MovieObject(
   items = [
      MediaObject(...)
   ]
)"""
        super(self, obj)       
        