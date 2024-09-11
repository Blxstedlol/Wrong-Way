import random
import requests
import sys
import os
import time
from colorama import Fore
import json

red = Fore.RED
green = Fore.GREEN
blue = Fore.BLUE
reset = Fore.RESET
def slow_print(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Most of this is just not needed but yk


health = 10
damage = 2
sword = 'Wooden Sword'
money = 0
level = 1



def write_data(data):
    with open('stats.json', 'w') as file:
        json.dump(data, file, indent=4)
def read_data():
    try:
        with open('stats.json', 'r') as file:
            data = json.load(file)
            return data
    except json.decoder.JSONDecodeError as e:
        write_data(player)
played_before = input(f'{blue}Played before? y/n:{reset}').lower()
if played_before == 'y':
    data = read_data()
    username = data['Username']
    level = data['Level']
    sword = data['Sword']
    money = data['Money']
    damage = data['Damage']
    health = data['Health']
    
if played_before == 'n':
    username = input(f'{green}Enter username: {reset}')
welcome_string = f'Welcome to The Wrong Way {username}'
slow_print(f'{blue}{welcome_string}{reset}')
player = {
    'Username': username,
    'Level': level,
    'Sword': sword,
    'Money': money,
    'Damage': damage,
    'Health': health
}

def reduce_health(amount):
    global health
    if health > 0:
        health -= amount
        if health < 0:
            health = 0  # Ensure health doesn't go below zero
def increase_level():
    global level
    level += 1
    return level
def increase_money(amount):
    global money
    money += amount
    return amount
def append_data(data):
    pass
def first_room():
    beat = False
    while beat is False:
        correct_way = random.choice(['w','a','s','d'])
        choice = input(f'{blue}What way will you go? W, A, S, D: {reset}').lower()
        correct_choices = ['w','a','s','d']
        if choice in correct_choices:
            if choice == correct_way:
                slow_print(f'{green}You found the candy store!')
                sword_change_chance = random.randint(1, 100)
                if sword_change_chance == 100:
                    player = {
                    'Username': username,
                    'Level': level,
                    'Sword': 'Candy Sword',
                    'Money': money,
                    'Damage': damage,
                    'Health': health
                        }
                    write_data(player)
                increase_money(random.randint(1, 5))
                increase_level()
                player = {
                    'Username': username,
                    'Level': level,
                    'Sword': sword,
                    'Money': money,
                    'Damage': damage,
                    'Health': health
                        }
                write_data(player)
            else:
                attacker = random.choice(['Zombie', 'Cat', 'Frog', 'Skeleton', 'Robot'])
                reduce_health(1)
                slow_print(f'{red}You got attacked by a {attacker}\n{green}Current Health: {health}{reset}')
                if health == 0:
                    slow_print(f'{red} You died{reset}')
                player = {
                    'Username': username,
                    'Level': level,
                    'Sword': sword,
                    'Money': money,
                    'Damage': damage,
                    'Health': health
                        }
                if level > 1:
                    beat = True
                    
                write_data(player)
def second_room():
            slow_print(f'{blue}Want to buy a medkit? this will restore your health to 10, Cost: $5{reset}')
            choice = input(f'{blue}y/n: {reset}').lower()
            if choice == 'y':
                    money =- 5
                    player = {
                    'Username': username,
                    'Level': level,
                    'Sword': sword,
                    'Money': money,
                    'Damage': damage,
                    'Health': 10
                    }
                    write_data(player)
            if choice == 'n':
                    pass
            correct_way = random.choice(['w', 'a', 's', 'd'])
            choice = input(f'{green}What way will you go? W, A, S, D: {reset}').lower()
            if correct_way == choice:
                slow_print(f'{green}Congrats! Level 2 has been completed{reset}')
                slow_print(f'{red}ALMOST{reset}')
                slow_print(f'{blue}First have a pet goat named jeffery!{reset}')
                slow_print(f'{blue}Now walk over to the fireplace by typing W{reset}')
                choice = input(f'{blue}Type W: ').lower()
                if choice == 'w':
                    data = read_data()
                    money = data['Money']
                    slow_print(f'{red}Now Kill jeffery for a new sword.{reset}')
                    slow_print(f'{red}Type E to kill jeffery.{reset}')
                    choice = input(f'{red}Type E: {reset}')
                    slow_print(f'{green}Wow! You did it! Level 3 time lets gooooo{reset}')
                    increase_level()
                    player = {
                    'Username': username,
                    'Level': level,
                    'Sword': 'G.O.A.T Slayer',
                    'Money': money,
                    'Damage': damage,
                    'Health': 10
                    }
                    write_data(player)
                    
            if correct_way != choice:
                 choice = input(f'{red}')
def room_calculation(level):
    if level == 1:
        first_room()
    if level == 2:
        second_room()
    if level == 3:
         slow_print('Game complete. Adding more levels weekly!')
if __name__ == '__main__':
        if played_before == 'y':
            data = read_data()
            level = data['Level']
            print(level)
            room_calculation(level)
            # need to finish doing rooms