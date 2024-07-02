# lib/cli.py
from models.fitness import Fitness
from models.exercise import Exercise

from helpers import (
    all_fitness,
    exit_program,
    add_fitness,
    add_exercise
)


def home():
    print()
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
            name = input("Please enter the training type: ")
            fitness = Fitness.find_by_name(name)
            if fitness:
                fit = fitness.id
                exercise = fitness.exercises()
                for i, ex in enumerate(exercise, start = 1):
                    print(f"{i}: {ex.name} | {ex.reps}")
                home3(fit)
            else:
                print("Training type was either entered innocorrectly, or does not exist.")
            home3()
        elif choice == "2":
            add_fitness()
        elif choice == "0":
            exit_program()
        else:
            print("Invalid Choice!") 

def home3(fit):
    print(fit)
    fitness_id = fit
    while True:
        print("Press 1 to add an exercise.")
        print("Press 2 to return to training types.")
        print("Press 3 to delete an exercise.")
        print("Press 0 to exit.")
        choice = input("> ")
        if choice == "1":
            add_exercise(fit)
        elif choice == "2":
            home2()
        elif choice == "3":
            del_exercise()
        elif choice == "0":
            exit_program()
        else:
            print("Invalid choice.")














if __name__ == "__main__":
    home()
    
    
