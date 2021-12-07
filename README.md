# Pixeldrain

A pixeldrain uploader and downloader made with pixeldrain api

## Installation

```
pip install Pixeldrain
```

## Usage

```py
import pixeldrain


# For upload file
pixeldrain.upload_file("file_path")
# returns upload details

# For get direct file
pixeldrain.download_file("file_id", "file_name")
# returns file name

# For get file link
file = pixeldrain.file("file_id")
# returns file link

# For information about the file
info = pixeldrain.info("file_id")
# returns information as json

# For get thumbnail
thumbnail = pixeldrain.thumbnail("file_id", width="", height="")
# returns thumbnail link
```
