"""Test Lib file"""
import pytest
from typer.testing import CliRunner

from video_downloader import cli

runner = CliRunner()


class TestCLI:
    def test_hello(self):
        output = runner.invoke(cli.app, "hello")
        assert output.exit_code == 0
        assert "Hello World" in output.stdout

    def test_goodbye(self):
        output = runner.invoke(cli.app, "goodbye")
        assert output.exit_code == 0
        assert "Good bye" in output.stdout


if __name__ == "__main__":
    pytest.main()
