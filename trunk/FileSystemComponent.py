__author__ = 'memonono'


class FileSystemComponent:

    def __init__(self, size, name, content):
        self.size = size
        self.content = content
        self.name = name

    def open(self):
        return self.content