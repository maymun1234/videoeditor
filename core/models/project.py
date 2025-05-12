import os
import json
from typing import List, Optional
from datetime import datetime
from .track import Track

class Project:
    FILE_EXTENSION = ".aydiv"

    def __init__(self, name: str, project_dir: Optional[str] = None):
        self.name: str = name
        self.project_dir: str = project_dir or os.path.join(
            os.path.expanduser("~/Documents/Aydınvideo/Projects"), name
        )
        self.tracks: List[Track] = []
        self.created_at: str = datetime.utcnow().isoformat()
        self.modified_at: str = self.created_at

    def add_track(self, track: Track):
        self.tracks.append(track)
        self._update_modified_time()

    def remove_track(self, track_index: int):
        if 0 <= track_index < len(self.tracks):
            del self.tracks[track_index]
            self._update_modified_time()
        else:
            raise IndexError(f"Track index {track_index} out of range")

    def clear(self):
        self.tracks.clear()
        self._update_modified_time()

    def _update_modified_time(self):
        self.modified_at = datetime.utcnow().isoformat()

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "created_at": self.created_at,
            "modified_at": self.modified_at,
            "tracks": [track.to_dict() for track in self.tracks],
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Project":
        proj = cls(name=data["name"])
        proj.created_at = data.get("created_at", proj.created_at)
        proj.modified_at = data.get("modified_at", proj.modified_at)

        if "project_dir" in data:
            proj.project_dir = data["project_dir"]

        for tdata in data.get("tracks", []):
            track = Track.from_dict(tdata)
            proj.tracks.append(track)
        return proj

    def save(self):
        os.makedirs(self.project_dir, exist_ok=True)
        with open(self.project_path, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, ensure_ascii=False, indent=4)
        self._update_modified_time()

    @classmethod
    def load(cls, path: str) -> "Project":
        if not os.path.isfile(path):
            raise FileNotFoundError(f"Project file not found: {path}")

        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        proj = cls.from_dict(data)
        proj.project_dir = os.path.dirname(path)
        return proj

    def __repr__(self):
        return f"<Project name={self.name!r} tracks={len(self.tracks)}>"
