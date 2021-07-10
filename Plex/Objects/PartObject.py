class PartObject:
    """Represents a part of a piece of media. Most MediaObject instances will usually only have one part, but can contain more if the media is split across several files or URLs. The client will play each part contiguously."""
    def __init__(self, **kwargs):
        self.key = str(kwargs.get("key"))
        """A string specifying the location of the part. This can be an absolute URL, or a callback to another function generated using Callback()."""
        
        self.duration = int(kwargs.get("duration") or 0)
        """An integer specifying the duration of the part, in milliseconds."""
        
        
def WebVideoURL(url):
    return url

def RTMPVideoURL(url, clip=None, clips=None, width=None, height=None, live=False):
    return url

def WindowsMediaVideoURL(url, width=None, height=None):
    return url





# testUrl = "http://plex.tv/123123-456456"
# testUrl1 = WebVideoURL(testUrl)
# testUrl2 = RTMPVideoURL(testUrl)
# testUrl3 = WindowsMediaVideoURL(testUrl)
# print(testUrl)
# print(testUrl1)
# print(testUrl2)
# print(testUrl3)