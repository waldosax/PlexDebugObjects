from Objects.ObjectContainer import ObjectContainer

class _Agent:
    pass

    def start(self):
        pass

    def search(self, results: ObjectContainer, media, lang: str, manual: bool):
        pass

    def update(self, metadata, media, lang: str, force: bool):
        pass

class TV_Shows(_Agent):
    pass

class Movies(_Agent):
    pass
