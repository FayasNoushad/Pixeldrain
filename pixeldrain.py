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


def info(file_id):
    info = requests.get(f"https://pixeldrain.com/api/file/{file_id}/info")
    return info
