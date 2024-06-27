# lib/cli.py
from models.fitness import Fitness
from models.exercise import Exercise

from helpers import (
    all_fitness,
    exit_program,
    fitness_exercises
)


def home():
    while True:
        print()
        print()
        print("********************Welcome To Your Fitness Manager********************")
        print()
        print()
        print()
        all_fitness()
        print()
        print()
        print()
        print("Press 1 to see all exercises in your training type.")
        print("Press 0 to exit")
        choice = input(">")
        if choice == "1":
            fitness_exercises()
            pass
        elif choice == "0":
            exit_program()
        else:
            print("Invalid Choice")










if __name__ == "__main__":
    home()
    
    
