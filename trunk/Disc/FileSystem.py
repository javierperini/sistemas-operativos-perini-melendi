from Disc.Folder import *


class FileSystem:

    def __init__(self):
        self.root = Folder(0, [], self, '/')

    def split_path(self, path):
        return path.split("/")

    def find(self, folder, name_list):
        name, names = name_list
        current_comp = folder.component_named(name)
        if names.empty:
            return current_comp
        else:
            return self.find(current_comp, names)

    def size(self):
        return self.root.size()

    def cd(self, path):
        return self.find(self.root, self.split_path(path))

    def mk_dir(self, path, folder_name):
        self.cd(path).add_component(Folder(0, [], path, folder_name))

    def rm(self, path, folder_name):
        self.cd(path).remove_component(folder_name)

