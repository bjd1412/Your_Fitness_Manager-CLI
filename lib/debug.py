#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.publisher import Publisher
from models.videogame import Videogame
import ipdb

def reset_database():
    Publisher.drop_table()
    Videogame.drop_table()
    Publisher.create_table()
    Videogame.create_table()
    
    Microsoft = Publisher.create("Microsoft", "Redmond, WA")
    EA = Publisher.create("Electronic Arts", "Redwood City, CA")
    Videogame.create("HALO 5", "Sci-fi/FPS", 2023, "XBOX", Microsoft.id)
    Videogame.create("Apex Legends", "Sci-fi/FPS", 2020, "XBOX, PC, Playstation", EA.id )





reset_database()
ipdb.set_trace()
