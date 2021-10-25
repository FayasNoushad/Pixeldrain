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
    Returns the full file associated with the ID.
    Supports byte range requests.
    
    file(file_id)
    """
    response = requests.get("https://pixeldrain.com/api/file/"+file_id)
    return response


def info(file_id):
    """
    Returns information about one or more files.
    You can also put a comma separated list of file IDs in the URL and it will return an array of file info, instead of a single object.
    
    info(file_id)
    """
    info = requests.get(f"https://pixeldrain.com/api/file/{file_id}/info")
    return info
