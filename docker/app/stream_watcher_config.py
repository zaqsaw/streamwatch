import os
import logging

from pathlib import Path
from configparser import ConfigParser


CONFIG_FILENAME="config.ini"


class StreamWatcherConfig:
    header = "DEFAULT"

    def __init__(self) -> None:
        self.config = ConfigParser()
        self.config[self.header] = {
            # The name of the channel to query
            "streamer": "",
            # The Oath Authorization can be gotten from a a browser developer console using
            # document.cookie.split("; ").find(item=>item.startsWith("auth-token="))?.split("=")[1]
            "auth": "",
            # The output path to save to
            "output_path": "/app/download",
            # The output filename to use
            "output_file": "stream.mp4",
            # The amount of time to wait in between queries, in seconds
            "period": "60",
        }

    @property
    def streamer(self) -> str:
        return self.config[self.header]["streamer"]

    @property
    def auth(self) -> str:
        return self.config[self.header]["auth"]

    @property
    def output_path(self) -> Path:
        return Path(self.config[self.header]["output_path"])

    @property
    def output_file(self) -> str:
        return self.config[self.header]["output_file"]

    @property
    def period(self) -> int:
        return int(self.config[self.header]["period"])

    @property
    def output_filepath(self) -> Path:
        return self.output_path / self.output_path

    def update(self) -> None:
        cwd = Path(os.getcwd())
        config_file = cwd / CONFIG_FILENAME
        if not config_file.is_file():
            logging.info("%s is not present", config_file)
            return

        self.config.read(str(config_file))
