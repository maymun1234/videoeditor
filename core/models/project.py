import os
import json
from typing import List, Optional
from datetime import datetime

from core.models.track import Track


class Project:
    """
    Video düzenleme projesini temsil eder.
    - name: Proje adı
    - project_dir: Projenin kaydedileceği kök dizin
    - tracks: Zaman çizelgesindeki katmanlar (Track nesneleri)
    - created_at / modified_at: Metadata
    """

    FILE_EXTENSION = ".aydiv"  # Proje dosyası uzantısı

    def __init__(self, name: str, project_dir: Optional[str] = None):
        self.name: str = name
        self.project_dir: str = project_dir or os.path.join(
            os.path.expanduser("~/Documents/Aydınvideo/Projects"), name
        )
        self.tracks: List[Track] = []
        self.created_at: str = datetime.utcnow().isoformat()
        self.modified_at: str = self.created_at

    @property
    def project_path(self) -> str:
        """Projeyi kaydedeceğimiz dosya yolu (JSON)."""
        return os.path.join(self.project_dir, f"{self.name}{self.FILE_EXTENSION}")

    def add_track(self, track: Track):
        """Yeni bir track ekler."""
        self.tracks.append(track)
        self._update_modified_time()

    def remove_track(self, track_index: int):
        """İndekse göre bir track siler."""
        if 0 <= track_index < len(self.tracks):
            del self.tracks[track_index]
            self._update_modified_time()
        else:
            raise IndexError(f"Track index {track_index} out of range")

    def clear(self):
        """Projeyi sıfırlar (tüm track’leri siler)."""
        self.tracks.clear()
        self._update_modified_time()

    def _update_modified_time(self):
        self.modified_at = datetime.utcnow().isoformat()

    def to_dict(self) -> dict:
        """Projeyi sözlüğe dönüştürür (JSON için)."""
        return {
            "name": self.name,
            "created_at": self.created_at,
            "modified_at": self.modified_at,
            "tracks": [track.to_dict() for track in self.tracks],
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Project":
        """JSON’dan Project nesnesi oluşturur."""
        proj = cls(name=data["name"])
        proj.created_at = data.get("created_at", proj.created_at)
        proj.modified_at = data.get("modified_at", proj.modified_at)

        # Dizini de data içinde verebiliriz, yoksa varsayılan
        if "project_dir" in data:
            proj.project_dir = data["project_dir"]

        # Trackleri yeniden oluştur
        for tdata in data.get("tracks", []):
            track = Track.from_dict(tdata)
            proj.tracks.append(track)
        return proj

    def save(self):
        """Projeyi diske kaydeder (JSON dosyası)."""
        os.makedirs(self.project_dir, exist_ok=True)
        with open(self.project_path, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, ensure_ascii=False, indent=4)
        self._update_modified_time()

    @classmethod
    def load(cls, path: str) -> "Project":
        """Dosyadan proje yükler."""
        if not os.path.isfile(path):
            raise FileNotFoundError(f"Project file not found: {path}")

        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        proj = cls.from_dict(data)
        # project_dir'i dosyanın bulunduğu klasör olarak güncelle
        proj.project_dir = os.path.dirname(path)
        return proj

    def __repr__(self):
        return f"<Project name={self.name!r} tracks={len(self.tracks)}>"
