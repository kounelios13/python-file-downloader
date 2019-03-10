# Simple Python File Downloader

This is a simple python file downloader

# How to use it

```python
from downloader.manager import FileManager

m = FileManager()
m.download_file(url,file_name) # Will download a file from url and save it with file_name 

```

# What's next

There are a lot to be done.
Some cool ideas are:

* Download a single file using threads
* Download many files together using threads
* Pause/Resume download