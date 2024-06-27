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

def fitness_exercises():
    idd = input()
    exercise = Fitness.exercises(idd)
    for i, ex in enumerate(exercise, start = 1):
        return exercise[int(i) - 1]
        print(f"{i}: {ex.name} | {ex.reps}")
    

def all_exercises():
    exercises = Exercise.get_all()
    for i, ex in enumerate(exercises, start =1):
        print(f"{i}: {ex.name} | {ex.repsh}")



    

