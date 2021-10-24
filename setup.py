import os
import pathlib
from setuptools import setup, find_packages


def requirements(file="requirements.txt") -> list:
    if os.path.isfile(file):
        with open(file, encoding="utf-8") as r:
            return [i.strip() for i in r]
    else:
        return []


file = pathlib.Path(__file__).parent

README = (file / "README.md").read_text()

setup(
    name="Pixeldrain",
    version="1.0.0",
    author="FayasNoushad",
    long_description=README,
    long_description_content_type="text/markdown",
    description="A pixeldrain python module using pixeldrain official api",
    license="MIT",
    url="https://github.com/FayasNoushad/Pixeldrain",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    install_requires=requirements(),
    python_requires=">=3.6"
)
