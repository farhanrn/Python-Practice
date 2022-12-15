class Hero:
    def __init__(self,name,health,attackpower):
        self.__name = name
        self.__health = health 
        self._attackpower = attackpower

    #  getter
    def getName(self):
        return self.__name
    def gethealth(self):
        return self.__health 
    
    # setter
    def diserang(self,serangpower):
        self.__health-= serangpower
# awal dari game
earthshaker = Hero("earthshacker",50,5)
print(earthshaker.__dict__)

# game berjalan 
print(earthshaker.__getName())
earthshaker.diserang(5)
print(earthshaker)