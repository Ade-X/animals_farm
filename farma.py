# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 18:35:15 2019

@author: AdeX
"""
import random
class Critter(object):
    """Wirtualny pupil"""
    def __init__(self, name, hunger, boredom):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
        
    def __pass_time(self, index=4):
        if index == 4:
            self.hunger += 1
            self.boredom += 1
        elif 0 <= index < 4:
            self.hunger += 2
            self.boredom += 2
        elif index > 4:
            self.hunger += 0.5
            self.boredom += 0.5
        
    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "szczęsliwy"
        elif 5 <= unhappiness <= 10:
            m = "zadowolony"
        elif 11 <= unhappiness <= 15:
            m = "poddenerwowany"
        else:
            m = "wciekły"
        return m
    
    def talk(self):
        print("Nazywam się ", self.name, " i jestem ", self.mood, " teraz\n")
        self.__pass_time()
    
    def eat(self, food = 4): 
        food = int(input("Ile jedzenia: "))
        print("Mniam, mniam. Dziękuję")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time(food)
        
    def play(self, fun = 4):
        fun = int(input("Jak długa zabawa w min: "))
        print("Gili, gili!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time(fun)
        
    def __str__(self):
        msg = "Imię zwierzaka: " + self.name + "\n"
        msg += "Stan najedzenia: " + str(self.hunger) + "\n"
        msg += "Stan znudzenia: " + str(self.boredom) + "\n"
        return msg
        
    
def main():
    my_pupils = []
    how_many = int(input("Jak wiele zwierzaków chcesz utworzyć? "))
    i = 0    
    while i != how_many:
        if len(my_pupils) < 5:
            crit_name = input("Jak chcesz nazwać swojego zwierzaka?: ")
            crit = Critter(crit_name, hunger=random.randint(0, 10), boredom=random.randint(0, 10))
            my_pupils.append(crit)
        i += 1
    
    choice = None
    while choice != "0":
        print(
                """
                Opiekun zwierzaka
                0 - wyjdź z programu
                1 - słuchaj swoich zwierzaków
                2 - nakarm swoje zwierzaki
                3 - pobaw się ze swoimi zwierzakami
                4 - przejżyj dane o zwierzakach
                5 - zobacz listę zwierzaków
                """
                )
        choice = input("Wybierasz: ")
        print()
        
        # wujdź z pętli
        if choice == "0":
            print("Do widzenia")
            
        # słuchaj swojego zwierzaka
        elif choice == "1":
            for pupil in my_pupils:
                pupil.talk()
            
        # nakarm swojego zwierzaka
        elif choice == "2":
            for pupil in my_pupils:
                print("Karmisz zwierzaka o imieniu", pupil.name)
                pupil.eat()
            
        # pobaw się ze zwierzakien
        elif choice == "3":
            for pupil in my_pupils:
                print("Bawisz się ze zwierzakiem o imieniu", pupil.name)
                pupil.play()
            
        # dane
        elif choice == "4":
            for pupil in my_pupils:
                print(pupil)
            
        elif choice == "5":
            print("Twoje zwierzaki to: \n")
            for pupil in my_pupils:
                print(pupil)
            
        # nieznany wybór
        else:
            print("\nNiestety ", choice, " nie jest prawidłowym wyborem")

main()
input("\nAby zakończyć program, nacisnij klawisz Enter")