import requests


class DownloadManager():
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

        header_name = 'Content-Length'
        size = int(self.__get_header__(url, header_name))
        return size

    def get_file_type(self, url):
        """
        Get content type from a url
        :param url: The url we want to ask its content type
        :return: type The content type
        """
        header_name = "Content-Type"
        type = self.__get_header__(url,header_name)
        return type

    def __get_header__(self, url, name):
        response = requests.head(url)
        headers = response.headers
        header = headers.get(name)
        return header
