
class Hero:
    #untuk si player 
    def __init__(self, name, health, attackpower, armornumber):
        self.name = name
        self.health = health
        self.attackpower = attackpower
        self.armornumber = armornumber
    
    def serang(self, lawan ):
        print(self.name + ' menyerang ' + lawan.name)
        lawan.diserang(self, self.attackpower)

    def diserang(self , lawan, attackpower_lawan):
        print(self.name + ' diserang ' + lawan.name)
        attacak_diterima = attackpower_lawan/self.armornumber
        print("Serangan terasa : ", str(attacak_diterima))
        self.health -= attacak_diterima
        print('darah ' + self.name + ' tersisa ' + str(self.health)) 
        

sniper = Hero('sniper',100,10,5)
rikimaru = Hero('rikimaru',100,5,10)

sniper.serang(rikimaru)
print("\n")
rikimaru.serang(sniper)

sniper = Hero('sniper',100,10,5)
rikimaru = Hero('rikimaru',100,5,10)

sniper.serang(rikimaru)
print("\n")
rikimaru.serang(sniper)
