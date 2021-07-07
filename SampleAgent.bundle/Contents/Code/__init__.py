def Start():
    print("Starting sample agent ...")

class SampleAgent(Agent.TV_Shows):
    def __init__(self, **kwargs):
        super().__init__()
        self.name = "SampleAgent"
        self.languages = ["en"]