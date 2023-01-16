# singleton design pattern is to ensure that only once instance of a class should be created

class Singleton(object):
    _instance = None

    @staticmethod
    def get_instance():
        if Singleton._instance:
            return Singleton._instance
        else:
            return Singleton()._instance


    def __init__(self):
        if not Singleton._instance:
            Singleton._instance = self
        else:
            raise Exception("being a singleton class, it can not be instantiated once")


if __name__ == "__main__":
    single = Singleton()
    print(single.get_instance())
    print(single.get_instance())
    print(single.get_instance())
    second = Singleton()