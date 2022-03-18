"""Test Lib file"""
import pytest

from video_downloader.lib import Playlist, VideoDownloader, YouTube


@pytest.fixture
def video():
    """return Youtube instance"""
    return VideoDownloader.video("https://www.youtube.com/watch?v=cnpJKdcwAMQ")


@pytest.fixture
def playlist():
    """return Playlist instance"""
    return VideoDownloader.playlist(
        url="https://www.youtube.com/watch?v=cnpJKdcwAMQ"
    )


class TestVideoDownloader:
    """Lib test class"""

    @staticmethod
    def test_video(video):
        """test video method"""
        assert isinstance(video, YouTube), "TypeError"

    @staticmethod
    def test_playlist(playlist):
        """test playlist method"""
        assert isinstance(playlist, Playlist), "TypeError"

    @staticmethod
    def test_download():
        """test download method"""
        assert VideoDownloader.download() is None, "TypeError"


if __name__ == "__main__":
    pytest.main()
