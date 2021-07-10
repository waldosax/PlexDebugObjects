from .PartObject import PartObject

class MediaObject:
    """Represents a single piece of media. Each metadata object may have multiple media objects associated with it. All media objects for the metadata object should refer to the same media, but in different formats, resolutions and/or containers (where available), allowing the client to choose the most appropriate item for playback."""
    def __init__(self, **kwargs):
        self.protocols = []
        """A list of strings specifying the protocols that the server and client must support in order to play the media directly. The list should contain values defined in Protocol."""
        if kwargs.get("protocols"):
            for item in kwargs["protocols"]:
                self.protocols.append(str(item))
        
        self.platforms = []
        """A list of strings specifying the client platforms the media item should be made available to. If the list is empty, the item will be available on all platforms. The list should contain values defined in Platform."""
        if kwargs.get("platforms"):
            for item in kwargs["platforms"]:
                self.platforms.append(str(item))
        
        self.bitrate = int(kwargs.get("bitrate")) if kwargs.get("bitrate") else None
        """An integer specifying the media's bitrate."""
        
        self.aspect_ration = float(kwargs.get("aspect_ration")) if kwargs.get("aspect_ration") else None
        """An integer specifying the media's aspect ratio (width / height)."""
        
        self.audio_channels = int(kwargs.get("audio_channels")) if kwargs.get("audio_channels") else None
        """An integer specifying the number of audio channels the media has (e.g. 2 for stereo, 6 for 5.1)."""
        
        self.audio_codec = str(kwargs.get("audio_codec"))
        """A string specifying the media's audio codec. This attribute should be set to one of the constants defined in AudioCodec."""
         
        self.video_codec = str(kwargs.get("video_codec"))
        """A string specifying the media's video codec. This attribute should be set to one of the constants defined in VideoCodec."""
        
        self.video_resolution = int(kwargs.get("video_resolution")) if kwargs.get("video_resolution") else None
        """An integer specifying the vertical resolution of the video."""
        
        self.container = str(kwargs.get("container"))
        """A string specifying the media's container. This attribute should be set to one of the constants defined in Container."""
        
        self.video_frame_rate = int(kwargs.get("video_frame_rate")) if kwargs.get("video_frame_rate") else None
        """An integer representing the frame rate of the media."""
        
        self.duration = int(kwargs.get("duration") or 0)
        """An integer specifying the duration of the media, in milliseconds."""
        
        self.parts = []
        if kwargs.get("parts"):
            for item in kwargs["parts"]:
                if (isinstance(item, PartObject)):
                    self.parts.append(item)
        
        
        
    def add(self, obj):
        """Adds the PartObject instance obj to the media object's list of parts. The media object can also be populated by passing a list of objects to the constructor as the parts argument:

media = MediaObject(
  parts = [
    PartObject(...)
  ]
)"""
        if (isinstance(item, obj)):
            self.parts.append(obj)

