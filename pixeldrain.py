import requests


def upload_file(file):
    """
    Upload a file to pixeldrain
    
    upload_file(file)
    """
    response = requests.post(
        "https://pixeldrain.com/api/file",
        data={"anonymous": True},
        files={"file": open(file, "rb")}
    )
    return response


def file(file_id):
    """
    Returns direct file link
    
    file(file_id)
    """
    return "https://pixeldrain.com/api/file/"+file_id


def download_file(file_id, file_name):
    """
    Download the full file associated with the ID.
    Supports byte range requests.
    
    download_file(file_id, file_name)
    """
    response = requests.get(file(file_id))
    with open(file_name, "wb") as file:
        file.write(response.content)
    return file_name


def info(file_id):
    """
    Returns information about one or more files.
    You can also put a comma separated list of file IDs in the URL and it will return an array of file info, instead of a single object.
    
    info(file_id)
    """
    info = requests.get(f"https://pixeldrain.com/api/file/{file_id}/info")
    return info


def thumbnail(file_id, width="", height=""):
    """
    Returns a PNG thumbnail image representing the file.
    The thumbnail image will be 128x128 px by default.
    You can specify the width and height with parameters in the URL.
    The width and height parameters need to be a multiple of 16.
    So the allowed values are 16, 32, 48, 64, 80, 96, 112 and 128.
    If a thumbnail cannot be generated for the file you will be redirected to a mime type image of 128x128 px.
    
    thumbnail(file_id, width, height)
    width and height is optional
    """
    api = f"https://pixeldrain.com/api/file/{file_id}/thumbnail"
    api += "?" if width or height else ""
    api += "width=" + width if width else ""
    api += "&" if width and height else ""
    api += "height=" + height if height else ""
    thumbnail = requests.get(api)
    return thumbnail
