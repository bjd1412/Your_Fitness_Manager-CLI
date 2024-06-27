#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.fitness import Fitness
from models.exercise import Exercise
import ipdb

def reset_database():
    Fitness.drop_table()
    Exercise.drop_table()
    Fitness.create_table()
    Exercise.create_table()
    
    Cardio = Fitness.create("Cardio", "Heart/Weightloss/legs")
    Strength = Fitness.create("Strength", "Arms/Chest/Back/Legs")
    Endurance = Fitness.create("Endurance", "Full Body")
    Balance = Fitness.create("Balance", "Full Body")

    Incline = Exercise.create("High-Incline Power Walk", "30 min", Cardio.id)
    Run = Exercise.create("Jogging", "1 hour", Cardio.id)
    HIT = Exercise.create("HIIT", "45 min", Endurance.id)
    Box = Exercise.create("Box Jumps", "3 sets pf 10", Endurance.id)
    Barbell = Exercise.create("105lb Barbell press", "3 sets of 12", Strength.id)
    Pushups = Exercise.create("Push-ups", "4 sets of 25", Strength.id)
    Dumbell = Exercise.create("25lb Dumbell Curls", "3 sets of 15", Strength.id)
    Shifts = Exercise.create("Weight-shifts", "60 seconds", Balance.id)
    Single = Exercise.create("Single Leg Bicep Curl", "60 seconds", Balance.id)






reset_database()
ipdb.set_trace()
