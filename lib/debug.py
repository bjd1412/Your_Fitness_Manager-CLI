#!/usr/bin/env python3
# lib/debug.py

from __init__ import CONN, CURSOR
from publisher import Publisher
from videogame import Videogame
import ipdb

def reset_database():
    Publisher.drop_table()
    Publisher.create_table()
    Videogame.drop_table()
    Videogame.create_table()





reset_database()
ipdb.set_trace()
