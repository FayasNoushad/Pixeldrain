# Pixeldrain

A pixeldrain uploader and downloader made with pixeldrain api

## Installation

```
pip install Pixeldrain
```

## Usage

```py
import pixeldrain


pixeldrain.upload_file("file_path")
# For upload file

pixeldrain.download_file("file_id", "file_name")
# For get direct file

file = pixeldrain.file("file_id")
# For get file link

info = pixeldrain.info("file_id")
# For information about the file

thumbnail = pixeldrain.thumbnail("file_id", width="", height="")
# For get thumbnail
```
