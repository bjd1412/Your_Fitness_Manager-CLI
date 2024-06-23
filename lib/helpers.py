# lib/helpers.py
from models.fitness import  Fitness
from models.exercise import Exercise

#Fitness


def exit_program():
    print("Goodbye!")
    exit()

def list_all_fitness():
    fitness = Fitness.get_all()
    for i,fit in enumerate(fitness,start=1):
        print(f"{i}. {fit.training}")

def fitness_by_id():
    id_ = input()
    fit = Fitness.find_by_id(id_)
    if fit:
        print(fit)
    else:
        print("The fitness id was not found.")

def fitness_by_training():
    train = input("Enter the type of training: ")
    fit = Fitness.find_by_name(train)
    if fit:
        print(fit)
    else:
        print("The training type was not found.")

def create_fitness():
    training = input("Enter the training type: ")
    target = input("Enter the muscle you wish to target: ")
    try:
        fitness = Fitness.create(training, target)
        print(f"Successfully created game fitness training type.")
    except Exception as ex:
        print("Error creating fitness trainer: ", ex)

def delete_fitness():
    train = input("Enter the training type you wish to remove: ")
    if fitness := Fitness.find_by_name(train):
        fitness.delete()
        print(f"Fitness training type successfully deleted.")
    else:
        print(f"Training type was not found.")

def list_training_exercises():
    id_ = input("Enter the training numer: ")
    fitness = Fitness.find_by_id(id_)
    if fitness:
        exercises = fitness.exercises()
        for exercise in exercises:
            print(exercise)
    else:
        print(f"Training type doesnt exist yet.")

#Exercise 

def list_all_Exercises():
    exercise = Exercise.get_all()
    for ex in exercise:
        print(ex)

def find_exercise_by_name():
    name = input("Please enter the name of the exercise: ")
    exercise = Exercise.find_by_name(name)
    if exercise:
        print(exercise)
    else:
        print(f"The exercise {name} was not found")

def find_exercise_by_id():
    id_ = input("Please enter the video game id: ")
    exercise = Exercise.find_by_id(id_)
    if exercise:
        print(exercise)
    else:
        print(f"The video game id: {id_} was not found") 

def delete_exercise():
    id_ = input("Please enter the video game you wish to remove: ")
    if exercise:= Exercise.find_by_id(id_):
        exercise.delete()
        print("Removal was successful.")
    else:
        print(f"Error: Video game id: {id_} was not found.")


def create_exercise():
    name = input("Please enter the exercise name: ")
    reps = input("Please enter the repitition: ")
    try:
        exercise = Exercise.create(name, reps, fitness_id)
        print(f"Exercise {name} has been created and stored!")
    except Exception as ex:
        print("Exercise creation error: one or more of the fields were entered incorrectly: ", ex)
        


    

