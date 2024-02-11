# Pixeldrain

A pixeldrain uploader and downloader made with pixeldrain api

## Installation

```sh
pip3 install Pixeldrain
```

## Usage

```py
import pixeldrain


# To get information about the file
info = pixeldrain.info(file_id)
# returns information as raw data

# To get file link
file = pixeldrain.file(file_id)
# returns file link

# To upload file
pixeldrain.upload_file(file_path)
# returns upload details

# To download file
pixeldrain.download_file(file_id, file_name, file_path)
# returns file name
# "file_name" and "file_path" are optional

# To get thumbnail
thumbnail = pixeldrain.thumbnail(file_id, width, height)
# returns thumbnail link
# width and height are optional
```

---

## Thanks to

- [Pixeldrain API](https://pixeldrain.com/api)
- [Contributors](https://github.com/FayasNoushad/Pixeldrain/graphs/contributors)
