import random

# КЛАСС КОЛОД
class deck(object):
    
    def __init__(self, name, cards_id):
        self.name = name
        self.cards_id = cards_id
   
    def count_cards(self):
        return len(self.cards_id)
    
    def take_card(self):
        return random.choice(self.cards_id)

привет вася
    
# КЛАСС КАРТ

class card(object):
    
    def __init__(self, cid, name, description,actions, deck):
        self.cid = cid
        self.name = name
        self.description = description
        self.actions = actions
         
    def show_decks(self):
        return 

    def assign_card(self):
        return 
    
    def show_card(self):
        return 


### СОЗДАНИЕ КОЛОД

file = open('баланс_колод.txt', 'r', encoding="utf-8")
list_of_strings = []

x = file.readlines()
for i in x:
    y = i.split(';')
    list_of_strings.append(y)
    
list_of_decks = []
for i in list_of_strings:
    dec = deck(i[0],i[1:])
    list_of_decks.append(dec)
    
file.close()