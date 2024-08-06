# lib/cli.py
from models.fitness import Fitness
from models.exercise import Exercise

from helpers import (
    all_fitness,
    exit_program,
    add_fitness,
    add_exercise,
    delete_exercise,
    delete_fitness,
    fitness_exercises

)


def home():
    Fitness.create_table()
    Exercise.create_table()
    print()
    print("    Welcome to Your Fitness Manager")
    print("----------------------------------------")
    print()
    print()
    print("Enter 1 to see all of your training types.")
    print("Enter 0 to exit Your Fitness Manager.")
    while True:
        print()
        choice = input("> ")
        if choice == "1":
            home2()
        elif choice == "0":
            exit_program()
        else:
            print("Invalid Choice")

def home2():
    print()
    while True:
        print()
        print("          Your training types")
        print("----------------------------------------")
        print()
        all_fitness()
        print()
        print("----------------------------------------")
        print()
        print()
        print()
        print("Enter 1 to see all exercises for your training type.")
        print("Enter 2 to add a training type.")
        print("Enter 3 to delete your training type.")
        print("Enter 0 to exit Your Fitness Manager.")    
        choice = input("> ")
        if choice == "1":
            name = input("Please enter the training type: ")
            if fitness:= Fitness.find_by_name(name):
                fitness_exercises(fitness)
                home3(fitness)
            else:
                print("Invalid Choice!")
        elif choice == "2":
            add_fitness()
        elif choice == "3":
            delete_fitness()
        elif choice == "0":
            exit_program()
        else:
            print("Invalid Choice!") 

def home3(fitness):
    while True:
        print()
        print("Enter 1 to add an exercise.")
        print("Enter 2 to return to training types.")
        print("Enter 3 to delete an exercise.")
        print("Enter 0 to exit.")
        choice = input("> ")
        if choice == "1":
            add_exercise(fitness)
            fitness_exercises(fitness)
        elif choice == "2":
            home2()
        elif choice == "3":
            delete_exercise()
        elif choice == "0":
            exit_program()
        else:
            print("Invalid choice.")



if __name__ == "__main__":
    home()
    
    
