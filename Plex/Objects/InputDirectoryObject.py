from .PopupDirectoryObject import PopupDirectoryObject

class InputDirectoryObject(PopupDirectoryObject):
    """Represents a container of objects generated from a query inputted by the user. The client will display an input dialog with the given prompt."""
    def __init__(self, **kwargs):
        super().__init__()
        self.prompt = str(kwargs.get("prompt"))
        """A string specifying the prompt that should be displayed to the user in the input dialog displayed after selecting the object."""
        
        