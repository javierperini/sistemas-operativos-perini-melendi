class FileSystemComponent(object):

    def __init__(self, size, name, content):
        self.size = size
        self.name = name
        self.content = content

    def open(self):
        return self.content
