```
Made with Python3
(C) @FayasNoushad
Copyright permission under MIT License
License -> https://github.com/FayasNoushad/Pixeldrain/blob/main/LICENSE
```

---

## Installation

```
pip install Pixeldrain
```

---

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

---

## Credits

- [Fayas Noushad](https://github.com/FayasNoushad)
- [Pixeldrain API](https://pixeldrain.com/api)

---
