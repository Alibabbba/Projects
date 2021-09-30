# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 12:45:55 2021

@author: Mikołaj
"""

from random import randint


class Hero:
    def __init__(self, name="John", age=20):
        self.name = name
        self.age = age
        self.health = round(1000 / self.age)
        self.damage = 3
        self.speed = 5

    def stats(self):
        print(f"Hello, I'm {self.name}")
        print(f"My age is {self.age}")
        print(f"My health is {self.health}")

    def attack(self):
        damage = self.damage + randint(1, 4)
        return damage

    def hit(self, hit):
        self.health = self.health - hit
        print(f"{hero.name} lost {hit}HP")


class Monster:
    def __init__(self, name, health, damage, defence, speed):
        self.name = name
        self.health = health
        self.damage = damage
        self.defence = defence
        self.speed = speed

    def attack(self):
        damage = self.damage + randint(1, 4)
        return damage

    def hit(self, hit):
        self.health = self.health - hit
        print(f"{monster.name} lost {hit}HP")


class encounter:
    def __init__(self, hero, monster):
        print("Run or fight?(r/f)")
        for end in range(5):
            decision = input()
            if decision == "r":
                if self.run(hero, monster) is True:
                    return print("Escape succesfull")
                else:
                    print("Escape unsuccesfull")
                    self.fight(hero, monster)
                    return print(f"Hero health: {hero.health}\nMonster health: {monster.health}")
            elif decision == "f":
                self.fight(hero, monster)
                return print(f"Hero health: {hero.health}\nMonster health: {monster.health}")

            else:
                print("Unsupported input")
                if end == 4:
                    if self.run(hero, monster) is True:
                        return print("Escape succesfull")
                    else:
                        self.fight(hero, monster)
                        return print(f"Hero health: {hero.health}\nMonster health: {monster.health}")

    @staticmethod
    def fight(hero, monster):
        while hero.health > 0 and monster.health > 0:
            print("")
            if hero.speed > monster.speed:
                print(f"{hero.name} health: {hero.health}")
                print(f"{monster.name} health: {monster.health}")
                print(f"{hero.name} attacks")
                monster.hit(hero.attack())
                print(f"{monster.name} attacks")
                hero.hit(monster.attack())
            else:
                print(f"{monster.name} attacks")
                hero.hit(monster.attack())
                print(f"{hero.name} attacks")
                monster.hit(hero.attack())

    @staticmethod
    def run(hero, monster):
        print("Trying to run...")
        if hero.speed == monster.speed:
            return True if randint(0, 1) == 1 else False
        return True if hero.speed > monster.speed else False


if __name__ == "__main__":
    hero = Hero("John", 30)
    monster = Monster("Goblin", 50, 4, 3, 5)

    print(hero.__dict__)
    print(monster.__dict__)

    encounter(hero, monster)
