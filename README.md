upld.py
=========

Small python script to quickly upload a file to a remote destintion (typically a web server)
and get the public URL for sharing a file quickly to your own server.

```
usage: upld.py [-h] [-n Filename] [-c] File

Quick upload a file.

positional arguments:
  File         File to upload

optional arguments:
  -h, --help   show this help message and exit
  -n Filename  Destination filename
  -c           Copy the URL to the clipboard

```

Main configuration variables are located at the top of the script.

Implementation of the `upload_file` function can be easily modified to suit your needs. Right now it does a system call to scp.

Expects to run on python 3

For the copy to clipboard functinality it uses a python package called [clipboard](https://pypi.python.org/pypi/clipboard/0.0.4) This is the only extenal dependency.
