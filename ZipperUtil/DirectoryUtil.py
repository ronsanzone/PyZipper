import os

class DirectoryUtil:
    def __init__(self, base_directory):
        self.base_directory = base_directory

    def list_file_names(self):
        for filename in os.listdir(self.base_directory):
            yield filename

    def list_full_file_names(self):
        for root, dirs, files in os.walk(self.base_directory):
            for f in files:
                yield os.path.join(root, f)
