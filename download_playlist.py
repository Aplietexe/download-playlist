from argparse import ArgumentParser
from os import wait
from subprocess import DEVNULL, Popen

from pytube import Playlist

arg_parser = ArgumentParser()
arg_parser.add_argument(
    "url",
    help="YouTube Playlist URL",
    type=str,
)
arg_parser.add_argument(
    "--concurrency",
    help="Number of concurrent downloads",
    default=5,
    type=int,
)
args = arg_parser.parse_args()
url = args.url
concurrency = args.concurrency


playlist = Playlist(url)
processes = set()
counter = 0
for video in playlist.video_urls:
    processes.add(Popen(["pytube", video], stdout=DEVNULL))
    while len(processes) >= concurrency:
        wait()
        finished = {p for p in processes if p.poll() is not None}
        if finished:
            counter += len(finished)
            print(f"Finished {counter}/{len(playlist.video_urls)}")
            processes.difference_update(finished)
