from .Media import Media
from .Model.MetadataModel import MetadataModel
from .Objects.ObjectContainer import ObjectContainer

class _Agent:
    def __init__(self, **kwargs):
        self.name = str(kwargs.get("name"))
        """A string defining the name of the agent for display in the GUI. This attribute is required."""
        
        self.languages = []
        """A list of strings defining the languages supported by the agent. These values should be taken from the constants defined in the Locale API. This attribute is required."""
        if kwargs.get("languages"):
            for item in kwargs["languages"]:
                self.languages.append(str(item))
        
        self.primary_provider = bool(kwargs.get("primary_provider") or False)
        """A boolean value defining whether the agent is a primary metadata provider or not. Primary providers can be selected as the main source of metadata for a particular media type. If an agent is secondary (primary_provider is set to False) it will only be able to contribute to data provided by another primary agent. This attribute is required"""
        
        self.fallback_agent = str(kwargs.get("fallback_agent"))
        """A string containing the identifier of another agent to use as a fallback. If none of the matches returned by an agent are a close enough match to the given set of hints, this fallback agent will be called to attempt to find a better match. This attribute is optional."""
        
        self.accepts_from = []
        """A list of strings containing the identifiers of agents that can contribute secondary data to primary data provided by this agent. This attribute is optional."""
        if kwargs.get("accepts_from"):
            for item in kwargs["accepts_from"]:
                self.accepts_from.append(str(item))
        
        self.contributes_to = []
        """A list of strings containing the identifiers of primary agents that the agent can contribute secondary data to. This attribute is optional."""
        if kwargs.get("contributes_to"):
            for item in kwargs["contributes_to"]:
                self.contributes_to.append(str(item))
        
        

    def search(self, results, media, lang, manual):
        """Searching for results to provide matches for media

When the media server needs an agent to perform a search, it calls the agent's search method:

    search(self, results, media, lang, manual)¶
    Parameters:	
        self – A reference to the instance of the agent class.
        results (ObjectContainer) – An empty container that the developer should populate with potential matches.
        media (Media) – An object containing hints to be used when performing the search.
        lang (str) – A string identifying the user's currently selected language. This will be one of the constants added to the agent's languages attribute.
        manual (bool) – A boolean value identifying whether the search was issued automatically during scanning, or manually by the user (in order to fix an incorrect match)"""
        pass

    def update(self, metadata, media, lang, force):
        """Adding metadata to media

Once an item has been successfully matched, it is added to the update queue. As the framework processes queued items, it calls the update method of the relevant agents.

    update(self, metadata, media, lang)::
    Parameters:	
        self – A reference to the instance of the agent class.
        metadata – A pre-initialized metadata object if this is the first time the item is being updated, or the existing metadata object if the item is being refreshed.
        media (Media) – An object containing information about the media hierarchy in the database.
        lang (str) – A string identifying which language should be used for the metadata. This will be one of the constants defined in the agent's languages attribute.
        force (bool) – A boolean value identifying whether the user forced a full refresh of the metadata. If this argument is True, all metadata should be refreshed, regardless of whether it has been populated previously."""
        pass

class TV_Shows(_Agent):
    pass

class Movies(_Agent):
    pass

class Artist(_Agent):
    pass

class Album(_Agent):
    pass
