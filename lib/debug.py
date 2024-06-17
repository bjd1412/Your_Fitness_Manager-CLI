#!/usr/bin/env python3
# lib/debug.py

from __init__ import CONN, CURSOR
from publisher import Publisher
import ipdb

def reset_database():
    Publisher.drop_table()
    Publisher.create_table()





reset_database()
ipdb.set_trace()
