import MetadataObject
#import MovieObject
#import TVShowObject


class ObjectContainer:
    """A container for other objects. ObjectContainer is the type most frequently returned to other applications. It provides clients with an ordered list of items in response to a request."""
    def __init__(self, **kwargs):
        self.view_group = str(kwargs.get("view_group"))
        """A string specifying the name of the view group the client should use when displaying the container's contents. This should be the name of a group previously registered with Plugin.AddViewGroup()."""

        self.content = str(kwargs.get("content"))
        """Identifies the type of the objects inside the container. This attribute should be set to one of the container type constants identified here. ..todo: to container types"""

        self.art = str(kwargs.get("art"))
        """A string specifying an image resource that should be used as the container's background art."""

        self.title1 = str(kwargs.get("title1"))
        """A string specifying the first title to display in the user interface."""

        self.title2 = str(kwargs.get("title2"))
        """A string specifying the second title to display in the user interface."""

        self.http_cookies = str(kwargs.get("http_cookies"))
        """A string specifying any HTTP cookies that need to be passed to the server when attempting to play items from the container."""

        self.user_agent = str(kwargs.get("user_agent"))
        """A string specifying the user agent header that needs to be sent to the server when attempting to play items from the container."""

        self.no_history = bool(kwargs.get("no_history") or False)
        """A boolean specifying whether the container should be added to the client's history stack. For example, if Container B in the sequence A => B => C had no_cache set to True, navigating back from C would take the user directly to A."""

        self.replace_parent = bool(kwargs.get("replace_parent") or False)
        """A boolean specifying whether the container should replace the previous container in the client's history stack. For example, if Container C in the sequence A => B => C had replace_parent set to True, navigating back from C would take the user directly to A."""

        self.no_cache = bool(kwargs.get("no_cache") or False)
        """A boolean indicating whether the container can be cached or not. Under normal circumstances, the client will cache a container for use when navigating back up the directory tree. If no_cache is set to True, the container will be requested again when navigating back."""

        self.mixed_parents = bool(kwargs.get("mixed_parents") or False)
        """A boolean indicating that the objects in the container do not share a common parent object (for example, tracks in a playlist)."""

        self.header = []
        """The header and message attributes are used in conjunction. They instruct the client to display a message dialog on loading the container, where header is the message dialog's title and message is the body."""
        if kwargs.get("header"):
            for item in kwargs["header"]:
                self.header.append(str(item))

        self.message = []
        """The header and message attributes are used in conjunction. They instruct the client to display a message dialog on loading the container, where header is the message dialog's title and message is the body."""
        if kwargs.get("message"):
            for item in kwargs["message"]:
                self.message.append(str(item))

        self.objects = []
        if kwargs.get("objects"):
            for item in kwargs["objects"]:
                if (isinstance(item, MetadataObject)):
                    self.objects.append(str(item))

    def add(self, obj):
        """Adds the object obj to the container. The container can also be populated by passing a list of objects to the constructor as the objects argument:

oc = ObjectContainer(
  objects = [
    MovieObject(
      title = "Movie"
    ),
    VideoClipObject(
      title = "Video Clip"
    )
  ]
)
  """
        self.objects.append(obj)
    
    @staticmethod
    def len(container):
        """Containers can be passed to the len() function to get the number of objects they contain."""
        return len(container.objects)








# tv = TVShowObject(title="Sanford & Son")
# container = ObjectContainer(
#     title1="foo",
#     objects = [tv]
#   )
# movie = MovieObject(title="The Godfather")
# container.add(movie)
# print (ObjectContainer.len(container))