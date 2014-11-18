from FileSystemComponent import FileSystemComponent

__author__ = 'memonono'


class Folder(FileSystemComponent):

    def __init__(self, size, content, parent, name):
        super(size, name, content)
        self.parent = parent

    def parent(self):
        return self.parent

    def add_component(self,component):
        self.content.add(component)

    def remove_component(self,component):
        self.content.remove(component)