# lib/Videogame.py
from __init__ import CONN, CURSOR
from publisher import Publisher

class Videogame:
    def __init__(self, name, genre, year, console, publisher_id, id=None):
        self.id = id
        self.name = name
        self.genre = genre
        self.year = year
        self.console = console
        self.publisher_id = publisher_id

    def __repr__(self):
        return(
            f"<Videogame {self.id}: {self.name}, {self.genre}, {self.year}, {self.console}, " +
            f"Publisher ID: {self.publisher_id}>"
        )

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXIST videogames(
            id INTEGER PRIMARY KEY,
            name TEXT,
            genre TEXT,
            year INTEGER,
            console TEXT,
            publisher_id INTEGER,
            FOREIGN KEY (publisher_id) REFERENCES publishers(id))
            """
            CURSOR.execute(sql)
            CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """
        DROP TABLE IF EXISTS videogames;
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        sql = """
            INSERT INTO videogames(name, genre, year, console, publisher_id)
            """
        CURSOR.execute(sql,(self.name, self.genre, self.year, self.console, self.publisher_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, genre, year, console, publisher_id):
        videogame = cls(name, genre, year, console, publisher_id)
        videogame.save()
        return videogame

    def update(self):
        sql = """
            UPDATE videogames SET name = ?, genre = ?, year = ?, console = ?, publisher_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.genre, self.year, self.console, self.publisher_id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM videogames WHERE id = ?
        """
        CURSOR.execute(sql,(self.id,))




            
        