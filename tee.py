import sys
class Tee(object):
    def __init__(file_name, mode):
        self._file = open(file_name, mode)

    def __enter__(self):
        return self

    def __exit__(self):
        self.__close()

    def __flush(self):
        sys.stdout.flush()
        self._file.flush()

    def __close(self):
        self.flush()

    def write(self, data):
        sys.stdout.write(data)
        self._file.write(data)

    def writeln(self, data):
        self.write(data + "\n")