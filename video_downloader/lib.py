from pytube import YouTube, Playlist


class VideoDownloader:

    @staticmethod
    def video(url: str):
        return YouTube(url)

    @staticmethod
    def playlist(url: str):
        return Playlist(url)

    @staticmethod
    def download():
        ...
