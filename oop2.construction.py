class Hero: #template

    def __init__(self, inputname, inputhelath, inputpower, inputarmor):
        self.name = inputname
        self.health = inputhelath
        self.power = inputpower
        self.armor = inputarmor

#self itu sebagai hero 1
hero1 = Hero("sniper",100,10,4)
hero2 = Hero("mirana",100,15,1)
hero3 = Hero("ucup",1000,100,0)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)

