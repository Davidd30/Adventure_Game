# To import time
import time
import random

obstacles = [' lion ', ' tiger ', ' gorilla ']
support = [' gun ', ' rock ', ' knife ', ' big wood ']
result = [' victory ', ' defeat ']
animal = random.choice(obstacles)
weapon = random.choice(support)


def pause(mes):
    print(mes)
    time.sleep(3)


def intro():
    pause('Welcome player')
    pause('your mission is reach to the safe zone')
    pause('you are in the red zone and your car break down again')
    pause('In front of you a jungle full with wild animals')
    pause('behind you the toxic red zone')
    pause('you must leave your car and run away to the jungle')
    pause("you are brave you can beat the animals...isn't you !!!!")


def start():

    begin = input('press go to start \n').lower()

    if begin.lower() == "go":

        the_game()

    else:

        error_1()


def error_1():

    _1 = input('wirte it well ,please').lower()

    if _1.lower() == "go":

        start()

    else:
        error_1()


def the_game():

    pause('you ran fast and and you dropped....suddenly you see a'+animal)
    pause('in the right side you saw a'+weapon)
    pick()


def pick():

    main_question = input('pick it or run??????').lower()

    if main_question.lower() == "pick":

        pause("good choice and nice hit you hit the"+animal)

        ask_play_again()

    elif main_question.lower() == "run":

        pause("Ooohhh!! after minutes of running you being thirsty and dead")

        ask_play_again()

    else:
        error_2()


def error_2():
    _2 = input("type again to continue")

    if _2.lower() == "again":

        pick()

    else:
        error_2()


def ask_play_again():

    again = input("Do you want to play again.......(yes/no)").lower()

    if again.lower() == "yes":
        play_again()

    elif again.lower() == "no":
        pause("thank you for your time")
        exit()

    else:
        error_3()


def error_3():
    _3 = input("writ it well ,please").lower()

    if _3.lower() == "yes":
        ask_play_again()

    elif _3.lower() == "no":
        pause("thank you for your time")
        exit()

    else:
        error_3()


def play_again():
        pause("you enter a gokd mine and you see"+animal)
        pause('there was a'+weapon+"beside you")
        pick()


intro()

start()