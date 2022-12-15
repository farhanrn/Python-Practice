class Hero: #template
    # class variable 
    jumlah = 0

    def __init__(self, inputname, inputhelath, inputpower, inputarmor):
        # instance variable
        self.name = inputname
        self.health = inputhelath
        self.power = inputpower
        self.armor = inputarmor
        Hero.jumlah += 1
        print("Membuat hero dengan nama :" + inputname)

#self itu sebagai hero 1
hero1 = Hero("sniper",100,10,4)
print(Hero.jumlah)
hero2 = Hero("mirana",100,15,1)
print(Hero.jumlah)
hero3 = Hero("ucup",1000,100,0)
print(Hero.jumlah)


print(Hero.__dict__)

