from Disc import FileSystemComponent


class Folder(FileSystemComponent):

    def __init__(self, size, content, name, parent):
        self.parent = parent
        super(Folder).__init__(size, name, content)

    def parent(self):
        return self.parent

    def add_component(self, component):
        self.content.add(component)

    def remove_component(self, component):
        self.content.remove(component)

    def detect(self, name):
        for comp in self.content:
            if comp.name.equals(name):
                return comp
        return LookupError('File not found! :(')

    def component_named(self, name):
        self.content.detect(name)