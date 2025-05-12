from moviepy.editor import VideoFileClip
from pydub.utils import mediainfo

class MediaHandler:
    def __init__(self, media_file: str):
        self.media_file = media_file

    def get_duration(self) -> float:
        """Medya dosyasının süresini döndürür (ses ya da video)."""
        if self.media_file.endswith(('.mp4', '.avi', '.mov')):
            return self._get_video_duration()
        elif self.media_file.endswith(('.mp3', '.wav', '.flac')):
            return self._get_audio_duration()
        else:
            print("Desteklenmeyen dosya türü")
            return 0.0

    def _get_video_duration(self) -> float:
        """Video dosyasının süresini alır (saniye cinsinden)."""
        try:
            with VideoFileClip(self.media_file) as video:
                return video.duration
        except Exception as e:
            print(f"Video süresi alınırken bir hata oluştu: {e}")
            return 0.0

    def _get_audio_duration(self) -> float:
        """Ses dosyasının süresini alır (saniye cinsinden)."""
        try:
            info = mediainfo(self.media_file)
            return float(info['duration'])
        except Exception as e:
            print(f"Ses süresi alınırken bir hata oluştu: {e}")
            return 0.0
