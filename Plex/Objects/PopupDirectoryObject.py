from .DirectoryObject import DirectoryObject

class PopupDirectoryObject(DirectoryObject):
    """Similar to DirectoryObject above. The only difference is in the presentation of the directory’s content on the client - PopupDirectoryObjects are presented as a pop-up menu where possible, and are not added to the client’s history stack."""
    def __init__(self, **kwargs):
        super().__init__()