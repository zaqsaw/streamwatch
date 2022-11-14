import logging
import os
import subprocess

from configparser import ConfigParser
from enum import Enum
from streamlink import Streamlink
from streamlink import streams
from time import sleep
from typing import Dict
from typing import Sequence
from typing import Any

from stream_watcher_config import StreamWatcherConfig


logging.basicConfig(level=logging.INFO)


class TwitchStreams(Enum):
    AUDIO_ONLY="audio_only"
    WORST="worst"
    BEST="best"
    Q_160="160p"
    Q_360="360p"
    Q_480="480p"
    Q_720="720p60"
    Q_1080="1080p60"


stream_priority = [
    TwitchStreams.Q_1080,
    TwitchStreams.BEST,
]


def get_streams(auth: str, streamer: str) -> Dict[str, Any]:
    session = Streamlink({ "http-headers": f"Authentication=OAuth {auth}" })
    return session.streams(f"https://www.twitch.tv/{streamer}")


def get_priority_url(found_streams: Dict[str, Any]) -> str:
    for twitch_stream_name in stream_priority:
        if twitch_stream_name.value in found_streams:
            return found_streams[twitch_stream_name.value].url
    raise Exception("No prioritized stream found in list")


def download_stream(url: str, pathname: str) -> None:
    ffmpeg_cmd = ["ffmpeg", "-i", url, "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-c:a", "aac", "-b:a", "128k", pathname]
    subprocess.call(ffmpeg_cmd)


if __name__ == "__main__":
    twitch_streams: Dict[str, Any] = {}
    config = StreamWatcherConfig()

    while not twitch_streams:
        config.update()
        if not config.streamer:
            logging.info("No streamer set")
            sleep(config.period)
        else:
            twitch_streams = get_streams(config.auth, config.streamer)
            if not twitch_streams:
                logging.info(f"{config.streamer} is not live yet!")
                sleep(config.period)

    url = get_priority_url(twitch_streams)
    download_stream(url, str(config.output_filepath))
