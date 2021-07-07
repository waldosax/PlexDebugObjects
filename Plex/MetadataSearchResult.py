class MetadataSearchResult:
    """The MetadataSearchResult class includes the following attributes. Each attribute can be set by passing a keyword argument to the constructor, or setting the attribute directly on the object after it has been created."""
    def __init__(self, **kwargs):
        self.id = str(kwargs.get("id"))
        """A string that uniquely identifies the metadata. This can be in any format. The provided value will be passed to the update method if the metadata needs to be downloaded, so the developer should ensure that the value can be used later to access the metadata without the provided hints."""
        
        self.name = str(kwargs.get("name"))
        """A string defining the name of the matched metadata item. This will be displayed to the user if they choose to manually match a piece of media."""
        
        self.year = int(kwargs.get("year")) if kwargs.get("year") else None
        """An integer defining the year associated with the matched metadata item. This will be displayed to the user if they choose to manually match a piece of media, and can be helpful for identifying the correct item when two similarly or identically named results are returned."""
        
        self.score = int(kwargs.get("score") or 0)
        """An integer defining how close the result matches the provided hints. This should be a value between 0 and 100, with 100 being considered an exact match. Results with a score of 85 or greater are considered “good enough” for automatic matching, with the highest-scoring result being selected by default."""
        
        self.lang = str(kwargs.get("lang"))
        """A string defining the language of the metadata that would be returned by the given result. This should be equal to one of the constants defined in the Locale API."""
        
        