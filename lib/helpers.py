# lib/helpers.py
from models.fitness import  Fitness
from models.exercise import Exercise

#Fitness

def exit_program():
    print("Goodbye")
    exit()


def all_fitness():
    fitness = Fitness.get_all()
    for i, fit in enumerate(fitness, start = 1):
        print(f"{i}: {fit.training} | {fit.target}")

# def fitness_exercises():
#     id_ = input("Enter training id: ")
#     fitness = Fitness.find_by_id(id_)
#     if fitness:
#         exercise = fitness.exercises()
#         for i, ex in enumerate(exercise, start = 1):
#             print(f"{i}: {ex.name} | {ex.reps}")
#     else:
#         print("Nothing")   
         
    

def all_exercises():
    exercises = Exercise.get_all()
    for i, ex in enumerate(exercises, start =1):
        print(f"{i}: {ex.name} | {ex.repsh}")

def fitness_exercises():
    name = input("Please enter the training type: ")
    fitness = Fitness.find_by_name(name)
    if fitness:
        exercise = fitness.exercises()
        for i, ex in enumerate(exercise, start = 1):
            print(f"{i}: {ex.name} | {ex.reps}")
    else:
        print("Training type was either entered innocorrectly, or does not exist.")

def add_fitness():
    training = input("Please enter the name of your training type: ")
    target = input("Please enter the training types target target focus: ")
    try:
        Fitness.create(training, target)
        print("Fitness type succesfully created!")
    except:
        print("Failed to create fitness type. Please ensure you have entered in all details correctly.")

def add_exercise(fit):
    name = input("Please enter the exercise name: ")
    reps = input("Please enter the repetitions: ")
    fitness_id = fit
    try:
        exercise = Exercise.create(name, reps, fitness_id)
        print(f"Exercise {name} has been created and stored!")
    except Exception as ex:
        print("Exercise creation error: one or more of the fields were entered incorrectly: ", ex)


    
    



    

