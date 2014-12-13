from Disc.FileSystem import FileSystem


class Disc:
    def __init__(self):
        self.file_system = FileSystem()

    def save(self, path, _file):
        self.file_system.save(path, _file)

    def get(self, path):
        return self.file_system.cd(path)

    def used_disc(self):
        return self.file_system.size()



