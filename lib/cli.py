# lib/cli.py

from helpers import (
    exit_program,
    list_all_fitness,
    fitness_by_training,
    create_fitness,
    delete_fitness,
    list_all_Exercises,
    find_exercise_by_name,
    create_exercise,
    list_training_exercises,
    create_exercise
)

def homeMain():
    print("***************Welcome to the fitness manager!***************")
    print()
    print("Here are all of your training types:")
    print()
    list_all_fitness()
    print()
    print()
    print('Would you like to add a training type? press 1.')
    print("To exit, press 0") 
    print("Press 3 see all of your exsercises fo ryour training type.")   
    while True:
        choice = int(input())           
        if choice == 0:
            exit_program()
        elif choice == 1:
            list_training_exercises()
        elif choice == 3:
            menu2()






def main2():
    while True:
        menu2()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_all_Exercises()
        elif choice == "2":
            find_exercise_by_name()
        elif choice == "3":
            create_exercise()
        else:
            print("Invalid choice")


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_all_fitness()
        elif choice == "2":
            fitness_by_training()
        elif choice =="3":
            create_fitness()
        elif choice =="4":
            delete_fitness()



def menu():
    print("Welcome to the ")
    print("0. Exit the program")
    print("1. Some useful function")

def menu2():
    print("press 1 to go back to Home Menu")
    print("press 2 to add an exercise")
    while True:
        choice = input(">")
        if choice == "2":
            create_exercise()
        elif choice == "1":
            homeMain()





def mover():
    choice = 0
    print("Hey, for fitness 1 exercise 2 ")
    while True:
        choice = input(">")
        if choice == "1":
            main()
        elif choice == "2":
            main2()
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    homeMain()
    
    
