from FileSystem import FileSystem


class Disc:
    def __init__(self):
        self.records = []

    def save(self, path, _file):
        self.records.append((path, _file))

    def get(self, path):
        return filter(lambda (p, r): p.__comp__(path), self.records).__getitem__(0)

    def used_disc(self):
        used = 0
        for (path, record) in self.records:
            used += record.size()
        return used


