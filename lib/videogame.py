# lib/Videogame.py
from __init__ import CONN, CURSOR
from publisher import Publisher

class Videogame:
    all = {}
    
    def __init__(self, name, genre, year, console, publisher_id, id=None):
        self.id = id
        self.name = name
        self.genre = genre
        self.year = year
        self.console = console
        self.publisher_id = publisher_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, genre):
        if isinstance(genre, str) and len(genre):
            self._genre = genre
        else:
            raise ValueError("Genre must be a non-empty string")

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        if type(year) is int and int(year) >= 1950:
            self._year = year
        else:
            raise ValueError("Year must be an integer greater than 1950")

    @property
    def publisher_id(self):
        return self._publisher_id

    @publisher_id.setter
    def publisher_id(self, publisher_id):
        if type(publisher_id) is int and Publisher.find_by_id(publisher_id):
            self._publisher_id = publisher_id
        else:
            raise ValueError("The publisher's id must reference a publisher in the database")



    def __repr__(self):
        return(
            f"<Videogame {self.id}: {self.name}, {self.genre}, {self.year}, {self.console}, " +
            f"Publisher ID: {self.publisher_id}>"
        )

    @property
    def console(self):
        return self._console

    @console.setter
    def console(self, console):
        if isinstance(console, str) and len(console):
            self._console = console
        else:
            raise ValueError("Console must be a non-empty string")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS videogames(
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
            VALUES (?, ?, ?, ?, ?)
            """
        CURSOR.execute(sql, (self.name, self.genre, self.year, self.console, self.publisher_id))
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
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        videogame = cls.all.get(row[0])

        if videogame:
            videogame.name = row[1]
            videogame.genre = row[2]
            videogame.year = row[3]
            videogame.console = row[4]
            videogame.publisher_id = row[5]
        else:
            videogame = cls(row[1], row[2], row[3], row[4], row[5])
            videogame.id = row[0]
            cls.all[videogame.id] = videogame
        return videogame

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM videogames WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT * FROM videogames WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM videogames
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]




            
        