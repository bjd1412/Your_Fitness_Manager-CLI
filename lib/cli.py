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
    print('Press 1 to see all exercises for your training type.')
    print("Press 2 to add a new training type.") 
    print("Press 0 to exit.")   
    while True:
        choice = int(input())           
        if choice == 0:
            exit_program()
        elif choice == 1:
            list_training_exercises()
            menu2()
        elif choise == 2:
            create_fitness()


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
    
    
