# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты 
# оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# from random import ranndint
from random import randint
import random  

def take_candies(player:str, candies:int):
    max_candies = 28
    if candies < 28:
        max_candies = candies
    n_candies: int = 0
    while True:
        n_candies = int(input(f'игрок {player}, возьмите конфеты (от 1 до {max_candies}): '))
        if 0 < n_candies <= max_candies:
            break
    candies -= n_candies
    print(f'игрок {player} взял {n_candies} конфет')
    if candies == 0:
        print(f'игрок {player} победил!')
    return candies


def take_candies_bot(player:str, candies:int):
    max_candies = 28
    if candies < 28:
        max_candies = candies
    n_candies: int = 0
    
    if player == "Бот":
        # Ходит бот, число конфет случайно
        print("Ходит бот")
        if 28 < candies < 57:
            min_candies_1 = 29
            # max_candies_1 = 57
            n_bot_candies = candies - min_candies_1
            print(f"Бот случайно взял {n_bot_candies} конфет")
            candies = candies - n_bot_candies        
        elif candies < 29:
            n_bot_candies = max_candies
            print(f"Бот взял {n_bot_candies} конфет")
            print("Бот победил")    
            exit()           
        else:
            n_bot_candies = randint(1,max_candies)
            print(f"Бот случайно взял {n_bot_candies} конфет")
            candies = candies - n_bot_candies
        if candies == 0:
            print("Бот победил")   
            exit         
    else:       
        while True:
            n_candies = int(input(f'Ваш ход, возьмите (от 1 до {max_candies}): '))
            if 0 < n_candies <= max_candies:
                break
    
        candies -= n_candies
        print(f'Вы взяли {n_candies} конфет')
    if candies == 0:
        print(f'Вы победили!')
        exit()    

    return candies



  
    
def game_two_players():
    candies = 121
    print('Правила:\nНа столе лежит 2021 конфета.'
          ' Играют два игрока делая ход друг после друга.\n'
          ' Первый ход определяется жеребьёвкой.\n'
          ' За один ход можно забрать не более чем 28 конфет.')
    player_1 = input('Введите имя первого игрока: ')
    player_2 = input('Введите имя второго игрока: ')

    player = random.choice((player_1, player_2))
    print(f'Первым ходит игрок {player}')
    player_dict = {1: player}
    if player == player_1:
        player_dict[-1] = player_2
        # print(player_dict)
    else:
        player_dict[-1] = player_1
    print(player_dict)
    
    print(player_dict.get(1))
    count = 1
    while candies > 0:
        candies = take_candies(player, candies)
        print(f'на столе осталось {candies}')
        count *= -1
        player = player_dict.get(count)


def game_with_bot():
    candies = 121
    print('Правила:\nНа столе лежит 2021 конфета.'
          ' Играют два игрока делая ход друг после друга.\n'
          ' Первый ход определяется жеребьёвкой.\n'
          ' За один ход можно забрать не более чем 28 конфет.')
    player_1 = input('Введите имя : ')
    player_2 = "Бот"

    player = random.choice ((player_1, player_2))
    print(f'Первым ходит игрок {player}')
    player_dict = {1: player}
    if player == player_1:
        player_dict[-1] = player_2
        # print(player_dict)
    else:
        player_dict[-1] = player_1
    print(f"{player_dict} - ходит первым")
    
    print(player_dict.get(1))
    count = 1
    while candies > 0:
        candies = take_candies_bot(player, candies)
        print(f'на столе осталось {candies}')
        count *= -1
        player = player_dict.get(count)


def func():
    print('func from zd_2.py')
    print(__name__)


if __name__ == '__main__':
    # func()
    user_choise = input('Выберите вариант 1 - два игрока, 2 - игра с ботом, q - для выхода: ')
    if user_choise == '1':
        game_two_players()
    elif user_choise == '2':
        game_with_bot()
    elif user_choise == 'q':
        exit()