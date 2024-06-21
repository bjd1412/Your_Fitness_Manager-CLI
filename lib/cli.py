# lib/cli.py

from helpers import (
    exit_program,
    helper_1,
    list_all_publishers,
    find_publisher_by_id,
    find_publisher_by_name,
    update_publisher,
    delete_publisher,
    list_all_videogames,
    find_videogame_by_id,
    find_videogame_by_name,
    update_videogame,
    delete_videogame,
    create_videogame
)

def main2():
    while True:
        menu2()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "6":
            list_all_videogames()
        elif choice == "7":
            find_videogames_by_id()
        elif choice == "8":
            find_videogames_by_name()
        elif choice == "9":
            create_videogames()
        elif choice == "10":
            update_videogames()
        elif choice == "11":
            delete_videogames()
        else:
            print("Invalid choice")


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_all_publishers()
        elif choice == "2":
            find_publisher_by_id()
        elif choice =="3":
            find_publisher_by_name()
        elif choice =="4":
            update_publisher()
        elif choice == "5":
            delete_publisher()
            print("Invalid choice")


def menu():
    print("Welcome to the ")
    print("0. Exit the program")
    print("1. Some useful function")

def menu2():
    print("New Menu")

def mover():
    choice = 0
    print("Hey, are you a publisher or a game. 22 for publisher, 23 for game: ")
    while True:
        choice = input(">")
        if choice == "22":
            main()
        elif choice == "23":
            main2()
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    mover()
    
    
