class Calculator:
    def __init__(self, model, color, length, width):
        self.__model = model
        self.__color = color
        self.__length = length
        self.__width = width

    # Accessors [ getters & setters ]
    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    # Extra methods
    def calc_area(self):
        return self.__length * self.__width

    # static method: it is a method that doesn't depend on object attributes -
    #           its result must not change for the same parameters within any call from any object
    # Calling :  static method can call instance method ??   NOooooo :  
    # Calling :  instance method can call static method ??   Yeeees
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b


