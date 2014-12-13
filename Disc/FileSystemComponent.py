class FileSystemComponent(object):

    def __init__(self, name, content):
        self.name = name
        self.content = content

    def open(self):
        return self.content

    def component_named(self, name):
        pass

    def size(self):
        pass