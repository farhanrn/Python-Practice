
class Hero:
    jumlah_hero = 0

    def __init__(self, inputname, inputhealth, inputpower, inputarmor):
        #instance variabe
        self.name = inputname
        self.health = inputhealth
        self.power = inputpower
        self.armor = inputarmor
        Hero.jumlah_hero += 1 

    #void function = mentode tanpa return  tanpa argumen
    def siapa(self):
        print("namaku adalah " + self.name)
    
    # method dengan argumen
    def healthup(self,up):
        self.health += up
    
    #method dengan nilai
    def gethealth(self):
        return self.health


hero1 = Hero('sniper',100,10,5)
hero2 = Hero('mario bros',90,5,10)

hero1.siapa() #ingat def fungsi nya itu 'siapa'

hero1.healthup(10)

print(hero1.health)

print(hero1.gethealth())