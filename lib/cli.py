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
    find_videogames_by_id,
    find_videogames_by_name,
    update_videogames,
    delete_videogames,
    create_videogames
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            helper_1()
        elif choice == "2":
            list_all_publishers()
        elif choice == "3":
            find_publisher_by_id()
        elif choice =="4":
            find_publisher_by_name()
        elif choice =="5":
            update_publisher()
        elif choice == "6":
            delete_publisher()
        elif choice == "7":
            list_all_videogames()
        elif choice == "8":
            find_videogames_by_id()
        elif choice == "9":
            find_videogames_by_name()



        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")


if __name__ == "__main__":
    main()
