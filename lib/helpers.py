# lib/helpers.py
from models.fitness import  Fitness
from models.exercise import Exercise

def exit_program():
    print("Goodbye")
    exit()


def all_fitness():
    fitness = Fitness.get_all()
    for  fit in fitness:
        print(f"{fit.training} | {fit.target}")
        print()
    

def all_exercises():
    exercises = Exercise.get_all()
    for i, ex in enumerate(exercises, start =1):
        print(f"{ex.name} | {ex.repsh}")

def fitness_exercises(fitness):
    if fitness:
        print()
        print(f"     {fitness.training}")
        print("-------------------")
        print()
        exercise = fitness.exercises()
        for ex in exercise:
            print(f"{ex.name} | {ex.reps}")
            print()
        print("-------------------")

def add_fitness():
    training = input("Please enter the name of your training type: ")
    target = input("Please enter the training types target focus: ")
    try:
        Fitness.create(training, target)
        print("Fitness type succesfully created!")
    except:
        print("Failed to create fitness type. Please ensure you have entered in all details correctly.")

def add_exercise(fitness):
    name = input("Please enter the exercise name: ")
    reps = input("Please enter the repetitions: ")
    fitness_id = fitness.id
    if fitness_id:
        try:
            exercise = Exercise.create(name, reps, fitness_id)
            print(f"Exercise {name} has been created and stored!")
        except Exception as ex:
            print("Exercise creation error: one or more of the fields were entered incorrectly: ", ex)
    else:
        print("Error")

def delete_fitness():
    name = input("Enter the training type you would like to delete: ")
    fitness = Fitness.find_by_name(name)
    if fitness:
        fitness.delete()
        print("Traning type deleted!")
    else:
        print("I'm sorry, the training type you entered was incorrect, or does not exist.")



def delete_exercise():
    name = input("Please enter the name of the exercise you wish to delete: ")
    exercise = Exercise.find_by_name(name)
    if exercise:
        exercise.delete()
        print("Exercise deleted!")
    else:
        print("I'm sorry, the exercise was either entered incorrectly, or does not exist.")
        


    
    



    

