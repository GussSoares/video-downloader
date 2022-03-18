"""Test Lib file"""
import pytest

from video_downloader.lib import Playlist, VideoDownloader, YouTube


@pytest.fixture
def video():
    return VideoDownloader.video("https://www.youtube.com/watch?v=cnpJKdcwAMQ")


@pytest.fixture
def playlist():
    return VideoDownloader.playlist(
        url="https://www.youtube.com/watch?v=cnpJKdcwAMQ"
    )


class TestVideoDownloader:
    def test_video(self, video):
        assert isinstance(video, YouTube), "TypeError"

    def test_playlist(self, playlist):
        assert isinstance(playlist, Playlist), "TypeError"

    def test_download(self):
        assert VideoDownloader.download() is None, "TypeError"
