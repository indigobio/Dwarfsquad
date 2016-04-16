import hashlib
import os


class Batch(dict):

    required_fields = {
        'file': "",
        'checksum': ""
    }

    def __init__(self, path_to_batch_zip):
        dict.__init__({})
        self.batch_zip_path = path_to_batch_zip
        self.checksum = ""
        self._setup()

    def _setup(self):
        self.batch_zip_path = os.path.abspath(self.batch_zip_path)
        assert os.path.exists(self.batch_zip_path)
        with open(self.batch_zip_path, "rb") as f:
            self.checksum = hashlib.sha512(f.read()).hexdigest()

    def open(self):
        self.file = open(self.batch_zip_path, "rb")

    def dump(self):
        return {'file': self.file, 'checksum': self.checksum}

    def close(self):
        if "file" in self and isinstance(self.file, file):
            self.file.close()
            del self["file"]