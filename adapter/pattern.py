# Target interface
class MediaPlayer:
    def play(self, audio_type, filename):
        pass

# Adaptee class
class AdvancedMediaPlayer:
    def playVlc(self, filename):
        print("Playing VLC file:", filename)

    def playMp4(self, filename):
        print("Playing MP4 file:", filename)

# Adapter class
class MediaAdapter(MediaPlayer):
    def __init__(self, audio_type):
        if audio_type == "vlc":
            self.advanced_player = AdvancedMediaPlayer()
        elif audio_type == "mp4":
            self.advanced_player = AdvancedMediaPlayer()

    def play(self, audio_type, filename):
        if audio_type == "vlc":
            self.advanced_player.playVlc(filename)
        elif audio_type == "mp4":
            self.advanced_player.playMp4(filename)

# Concrete class implementing the target interface
class AudioPlayer(MediaPlayer):
    def play(self, audio_type, filename):
        if audio_type == "mp3":
            print("Playing MP3 file:", filename)
        elif audio_type == "vlc" or audio_type == "mp4":
            media_adapter = MediaAdapter(audio_type)
            media_adapter.play(audio_type, filename)
        else:
            print("Invalid media type:", audio_type)
