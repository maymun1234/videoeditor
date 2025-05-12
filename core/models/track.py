from .media import MediaHandler  # Media işleme işlemleri burada olacak

class Track:
    def __init__(self, media_file: str):
        self.media_file = media_file
        self.filters = []

    def get_media_duration(self) -> float:
        """Medya dosyasının süresini döndürür (ses ya da video)."""
        media_handler = MediaHandler(self.media_file)
        return media_handler.get_duration()

    def to_dict(self):
        return {
            "media_file": self.media_file,
            "filters": [f.to_dict() for f in self.filters]
        }

    @classmethod
    def from_dict(cls, data):
        track = cls(data["media_file"])
        track.filters = [Filter.from_dict(f) for f in data["filters"]]
        return track
