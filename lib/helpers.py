# lib/helpers.py
from models.publisher import  Publisher
from models.videogame import Videogame

#Publishers
def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()

def list_all_publishers():
    publishers = Publisher.get_all()
    for pub in publishers:
        print(pub)

def find_publisher_by_id():
    id_ = input("Enter the id number of the publisher: ")
    publishers = Publisher.find_by_id(id_)
    if publishers:
        print(publishers)
    else:
        print("The publisher id was not found.")

def find_publisher_by_name():
    comp_name = input("Enter the name of the publisher: ")
    pub = Publisher.find_by_name(comp_name)
    if pub:
        print(pub)
    else:
        print("The publisher name was not found.")

def create_publishers():
    comp_name = input("Enter the name of the publisher: ")
    location = input("Enter the name of the publisher's location: ")
    try:
        publisher = Publisher.create(comp_name, location)
        print(f"Successfully created game publisher.")
    except Exception as ex:
        print("Error creating publisher: ", ex)

def delete_publisher():
    id_ = input("Enter the id of the publisher you wish to remove: ")
    if publisher := Publisher.find_by_id(id_):
        publisher.delete()
        print(f"Publisher id:{id_} successfully deleted.")
    else:
        print(f"Publisher id:{id_} not found.")

def update_publisher():
    id_ = input("Enter the id of the publisher: ")
    if publisher:= Publisher.find_by_id(id_):
        try:
            company_name = input("Enter the new name of the publisher: ")
            publisher.company_name = company_name
            location = input("Enter the publisher's new location: ")
            publisher.location = location
        except Exception as ex:
            print(f"Error updating publisher: ", ex)
    else:
        print(f"Publisher id:{id_} not found.")

#Videogames 

def list_all_videogames():
    videogames = Videogame.get_all()
    for video in videogames:
        print(video)

def find_videogames_by_name():
    name = input("Please enter the name of the video game: ")
    videogames = Videogame.find_by_name(name)
    if videogames:
        print(videogames)
    else:
        print(f"The video game {name} was not found")

def find_videogames_by_id():
    id_ = input("Please enter the video game id: ")
    videogames = Videogame.find_by_id(id_)
    if videogames:
        print(videogames)
    else:
        print(f"The video game id: {id_} was not found") 

def update_videogames():
    id_ = input("Please enter video game id: ")
    if videogames:= Videogame.find_by_id(id_):
        try:
            name = input("Please enter video game name: ")
            videogames.name = name
            genre = input("Please enter the video game's genre: ")
            videogames.genre = genre
            year = input("Please enter the video game's release year: ")
            videogames.year = year
            console = input("Please enter the console(s) the video game released on: ")
            videogames.console = console
            videogames.update()
        except Exception as ex:
            print("Error, update unsuccessful: ", ex)
    else:
        print(f"Error: Video game id: {id_} was not found.")

    def delete_videogames():
        id_ = input("Please enter the video game you wish to remove: ")
        if videogames:= Videogame.find_by_id(id_):
            videogames.delete()
            print("Removal was successful.")
        else:
            print("Error: Video game id: {id_} was not found.")


    def create_videogames():
        name = input("Please enter the video game's name: ")
        genre = input("Please enter the video game's genre: ")
        year = input("Please enter the video game's release year")
        console = input("Please enter the console(s) the video game released on: ")
        publisher_id = int(input("Please enter the publisher's id: "))
        try:
            videogame = Videogame.create(name, genre, year, console, publisher_id)
            print(f"Video game {name} has been created and stored!")
        except Exception as ex:
            print("Video game creation error: one or more of the fields were entered incorrectly: ", ex)
        


    

