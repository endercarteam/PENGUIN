import pygame

Ejecutar = str

class Pet:
    def __init__(self, name:str, species:str, gender:str , hunger, joy) -> None:
        self.name = name
        self.species = species
        self.gender = gender
        self.hunger = hunger
        self.joy = joy
