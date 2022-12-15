class Hero: #template
    pass


hero1 = Hero() #object
hero2 = Hero()
hero3 = Hero()

hero1.name = "sniper"
hero1.health = 100

hero2.name = "sven"
hero2.health = 200

hero3.name = "ucup"
hero3.healh = 1000

print(hero1) #letak memorinya 
print(hero1.__dict__) #

#untuk akses
print(hero1.name)



