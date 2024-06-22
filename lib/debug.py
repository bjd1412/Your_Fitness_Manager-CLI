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
    Incline = Exercise.create("Cardio", "High-Incline Run", "30 min", Cardio.id)





reset_database()
ipdb.set_trace()
