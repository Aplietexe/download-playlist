# download_playlist.py

Download all videos from a Youtube playlist in parallel.

## Usage

Tested on Python 3.11.

Clone this repo and move into it

```shell
git clone https://github.com/Aplietexe/download-playlist && cd download-playlist
```

Create a virtual environment

```shell
python3.11 -m venv .venv
```

Activate the virtual environment

```shell
source .venv/vin/activate
```

Install the required dependencies

```shell
pip install -r requirements.txt
```

Run the script

```shell
python download_playlist.py https://www.youtube.com/playlist?list=...
```

## CLI

### `--concurrency`

- Number of concurrent downloads.
- Default: `5`
