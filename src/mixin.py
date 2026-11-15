class MixinPrint:
    def __init__(self):
        print(repr(self))

    def __repr__(self):
        parameters = ""
        for i in self.__dict__.values():
            parameters += "," + " " + str(i)
        return f"{self.__class__.__name__}, {parameters}"
