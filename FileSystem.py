from Folder import *

__author__ = 'camila'


class FileSystem:

    def __init__(self):
        self.root = Folder(0, [], self, '/')

    def find(self, folder, name_list):
        name, names = name_list
        current_comp = folder.component_named(name)
        if names.empty:
            return current_comp
        else:
            current_comp.find(names)

    def cd(self, path):
        self.find(self.root, self.split_path(path))

    def size(self):
        self.size()

    def mk_dir(self, path, folder_name):
        self.find(self.root, self.split_path(path)).add_component(Folder(0, [], path, folder_name))

    def rm(self, path, folder_name):
        self.find(self.root, self.split_path(path)).remove_component(folder_name)

    def split_path(self, path):
        return path.split("/")
