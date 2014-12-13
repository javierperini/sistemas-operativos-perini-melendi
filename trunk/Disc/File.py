from FileSystemComponent import *


class File(FileSystemComponent):

    def __init__(self, name, content):
        super(File, self).__init__(name, content)

    def write(self, content):
        self.content.append(content)

    def size(self):
        return self.content.size()

    def component_named(self, names):
        return LookupError("Error you cant search in files!")