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
            "streamer": "",
            "auth": "",
            "output_path": "/app/download",
            "period": "60",
            "quit": "",
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
    def period(self) -> int:
        return int(self.config[self.header]["period"])

    @property
    def quit(self) -> bool:
        return bool(self.config[self.header]["quit"])

    def update(self) -> None:
        cwd = Path(os.getcwd())
        config_file = cwd / CONFIG_FILENAME
        if not config_file.is_file():
            logging.info("%s is not present", config_file)
            return

        self.config.read(str(config_file))
