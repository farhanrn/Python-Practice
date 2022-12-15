class Hero:

    #class variabel
    jumlah = 0
    __privateJumlah = 0

    def __init__(self, name, health):
        self.name = name
        self.health = health

        # variabel instance private
        self.__private = 'private'

        # variabel instance protected
        self.__protected = "protected"


# ini variabel bebas diakses
lina = Hero("Lina", 100)

print(lina.__dict__)
print(Hero.__dict__)


