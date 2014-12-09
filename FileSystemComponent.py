__author__ = 'memonono'


class FileSystemComponent:

    def __init__(self, size, name, content):
        self.size = size
        self.name = name
        self.content = content

    def open(self):
        return self.content
