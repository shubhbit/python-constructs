
class FCPFile:
    def hello(self):
        print("hello from FCP")

class GoogleFile:
    def hello(self):
        print("hello from Google file")


class File:
    file_map = {"fcp": FCPFile,
                "gcp": GoogleFile}

    def get_instance(self, type):
        return self.file_map[type]()


if __name__ == "__main__":
    fcp = File().get_instance("fcp")
    fcp.hello()
    gcp = File().get_instance("gcp")
    gcp.hello()