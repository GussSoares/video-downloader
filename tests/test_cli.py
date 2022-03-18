"""Test Lib file"""
import pytest
from typer.testing import CliRunner

from video_downloader import cli

runner = CliRunner()


class TestCLI:
    """CLI test class"""

    @staticmethod
    def test_hello():
        """test hello command"""
        output = runner.invoke(cli.app, "hello")
        assert output.exit_code == 0
        assert "Hello World" in output.stdout

    @staticmethod
    def test_goodbye():
        """test goodbye command"""
        output = runner.invoke(cli.app, "goodbye")
        assert output.exit_code == 0
        assert "Good bye" in output.stdout


if __name__ == "__main__":
    pytest.main()
