from Folder import Folder

__author__ = 'memonono'


class FileSystem:

    def __init__(self):
        self.root = []

    def cd(self, path):
        self.root.find(path)
        #Parsear el path(si es un String y buscar cada parte recursivamente)

    def size(self):
        self.size()

    def mk_dir(self, path, folder_name):
        self.root.find(path).add(Folder.new(0, [], path, folder_name))

    def rm(self, path, folder_name):
        self.root.find(path).remove_component(folder_name)