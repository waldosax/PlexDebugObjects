class MediaPart:
    def __init__(self, **kwargs):
        self.file = str(kwargs.get("file"))
        """A string identifying path to the media file on disk."""
        
        self.openSubtitlesHash = str(kwargs.get("openSubtitlesHash"))
        """A string identifying the hash of the file, as used by OpenSubtitles.org.

Note

This attribute is only available for Movie and TV Show metadata searches."""
        
        