# core/models/track.py

class Track:
    def __init__(self, media_file: str):
        self.media_file = media_file
        self.filters = []  # Filtreler burada saklanır

    def add_filter(self, filter):
        self.filters.append(filter)

    def remove_filter(self, filter_name: str):
        self.filters = [f for f in self.filters if f.name != filter_name]

    def apply_filters(self):
        for filter in self.filters:
            # Filtreyi medya verisi üzerinde uygula
            pass

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
