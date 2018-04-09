class objeto(object):
    def __init__(self, name, other_name):
        self.name = name
        self.__name_privado = other_name
        
    def __str__(self):
        return self.name + self.__name_privado
