import requests


class FileManager():
    def __init__(self):
        pass

    def download_file(self, url, file_name):
        """
        Download a file from a url.Will not create parent directories in case they don't exist
        :param url: The url of the file
        :param file_name: File name in disk
        :return:
        """
        size = self.get_file_size(url)
        print("Downloading file with name {}.Size:{} bytes".format(file_name, size))
        content = requests.get(url).content
        with open(file_name, "wb") as fp:
            fp.write(content)

    def get_file_size(self, url):
        """
        Return size of data in url
        :param url: url to request
        :return: size Size in bytes
        """
        # Perform a HEAD request to get only the head of the request
        response = requests.head(url)
        headers = response.headers
        header_name = 'Content-Length'
        size = int(headers.get(header_name))
        return size
