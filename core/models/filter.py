# core/models/filter.py

class Filter:
    def __init__(self, name: str, parameters: dict):
        self.name = name
        self.parameters = parameters

    def apply(self, media_data):
        # Filtreyi medya verisi üzerinde uygula
        pass

    def to_dict(self):
        return {
            "name": self.name,
            "parameters": self.parameters
        }

    @classmethod
    def from_dict(cls, data):
        return cls(name=data["name"], parameters=data["parameters"])
