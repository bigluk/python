class User:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


    def __str__(self):
        return self.name + " " + self.surname


    def get_surname(self):
        return self.surname


    def get_name(self):
        return self.name


    def set_surname(self, surname):
        self.surname = surname


    def set_name(self, name):
        self.name = name