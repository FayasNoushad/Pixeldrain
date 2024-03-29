import os
import setuptools


def requirements(file="requirements.txt"):
    if os.path.isfile(file):
        with open(file, encoding="utf-8") as r:
            return [i.strip() for i in r]
    else:
        return []


def readme(file="README.md"):
    if os.path.isfile(file):
        with open(file, encoding="utf8") as r:
            return r.read()
    else:
        return ""


setuptools.setup(
    name="Pixeldrain",
    version="1.1.2",
    description="Pixeldrain API",
    long_description=readme(),
    long_description_content_type="text/markdown",
    license="MIT",
    author="Fayas Noushad",
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    project_urls={
        "Tracker": "https://github.com/FayasNoushad/Pixeldrain/issues",
        "Source": "https://github.com/FayasNoushad/Pixeldrain"
    },
    python_requires=">=3.6",
    py_modules=['pixeldrain'],
    packages=setuptools.find_packages(),
    zip_safe=False,
    install_requires=requirements()
)
