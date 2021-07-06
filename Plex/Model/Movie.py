from .MetadataModel import MetadataModel
from .Proxy import Proxy

class Movie(MetadataModel):
    """Represents a movie (e.g. a theatrical release, independent film, home movie, etc.)"""
    def __init__(self, **kwargs):
        super().__init__()
        self.genres = []
        """A set of strings specifying the movie’s genre."""
        if kwargs.get("genres"):
            for item in kwargs["genres"]:
                self.genres.append(str(item))
        
        self.tags = []
        """A set of strings specifying the movie’s tags."""
        if kwargs.get("tags"):
            for item in kwargs["tags"]:
                self.tags.append(str(item))
        
        self.collections = []
        """A set of strings specifying the movie’s genre."""
        if kwargs.get("collections"):
            for item in kwargs["collections"]:
                self.collections.append(str(item))
        
        self.duration = int(kwargs.get("duration")) if kwargs.get("duration") else None
        """An integer specifying the duration of the movie, in milliseconds."""
        
        self.rating = float(kwargs.get("rating")) if kwargs.get("rating") else None
        """A float between 0 and 10 specifying the movie’s rating."""
        
        self.original_title = str(kwargs.get("original_title"))
        """A string specifying the movie’s original title."""
        
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
        """A set of strings specifying the movie’s writers."""
        if kwargs.get("writers"):
            for item in kwargs["writers"]:
                self.writers.append(str(item))
        
        self.directors = []
        """A set of strings specifying the movie’s directors."""
        if kwargs.get("directors"):
            for item in kwargs["directors"]:
                self.directors.append(str(item))
        
        self.producers = []
        """A set of strings specifying the movie’s producers."""
        if kwargs.get("producers"):
            for item in kwargs["producers"]:
                self.producers.append(str(item))
        
        self.countries = []
        """A set of strings specifying the countries involved in the production of the movie."""
        if kwargs.get("countries"):
            for item in kwargs["countries"]:
                self.countries.append(str(item))
        
        self.posters = []
        """A container of proxy objects representing the movie’s posters. See below for information about proxy objects."""
        if kwargs.get("posters"):
            for item in kwargs["posters"]:
                if (isinstance(item, Proxy)):
                    self.posters.append(item)
        
        self.art = []
        """A container of proxy objects representing the movie’s posters. See below for information about proxy objects."""
        if kwargs.get("art"):
            for item in kwargs["art"]:
                if (isinstance(item, Proxy)):
                    self.art.append(item)
        
        self.themes = []
        """A container of proxy objects representing the movie’s theme music. See below for information about proxy objects."""
        if kwargs.get("themes"):
            for item in kwargs["themes"]:
                if (isinstance(item, Proxy)):
                    self.themes.append(item)
        
        
        
        