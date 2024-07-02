# lib/cli.py
from models.fitness import Fitness
from models.exercise import Exercise

from helpers import (
    all_fitness,
    exit_program,
    fitness_exercises,
    add_fitness
)


def home():
    print("********************Welcome To Your Fitness Manager********************")
    print()
    print()
    print("Press 1 to see all of your training types.")
    print("Press 0 to exit Your Fitness Manager.")
    while True:
        print()
        choice = input(">")
        if choice == "1":
            home2()
        elif choice == "0":
            exit_program()
        else:
            print("Invalid Choice")

def home2():
    print()
    print()
    print("***************")
    print()
    all_fitness()
    print()
    print("***************")
    print()
    while True:
        print()
        print()
        print("Press 1 to see all exercises for your training type.")
        print("Press 2 to add a training type.")
        print("Press 0 to exit Your Fitness Manager.")
    
        choice = input("> ")
        if choice == "1":
            fitness_exercises()
        elif choice == "2":
            add_fitness()
        elif choice == "0":
            exit_program()
        else:
            print("Invalid Choice!") 

def home3():
    pass












if __name__ == "__main__":
    home()
    
    
