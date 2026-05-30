class Player:
    def __init__(self, name):
        self.__name = name

    def who_am_i(self):
        return f"you are palyer {self.__name}"

    def get_name(self):
        return self.__name
