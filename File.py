from FileSystemComponent import *

__author__ = 'memonono'


class File(FileSystemComponent):

    def __init__(self, size, name, content):
        super(File).__init__(size, name, content)
       # super(File, self).__init__(size, name, content)


    def component_named(self, names):
        return LookupError("Error you cant search in files!")