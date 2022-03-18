"""Lib Video Downloader"""

from pytube import Playlist, YouTube


class VideoDownloader:
    """Video Downloader class"""

    @staticmethod
    def video(url: str):
        """return a YouTube instance with url passed"""
        return YouTube(url)

    @staticmethod
    def playlist(url: str):
        """return a Playlist instance with url passed"""
        return Playlist(url)

    @staticmethod
    def download():
        """Not implemented"""
        ...
