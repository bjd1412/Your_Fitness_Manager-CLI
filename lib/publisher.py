#lib/publisher.py
from __init__ import CURSOR, CONN



class Publisher:
    all = {}

    def __init__(self, company_name, location, id=None):
        self.id = id
        self.company_name = company_name
        self.location = location

    def __repr__(self):
        return f"<Publisher {self.id}: {self.company_name}, {self.location}>"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS publishers (
            id INTEGER PRIMARY KEY,
            company_name TEXT,
            location TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS publishers;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO publishers(company_name, location) VALUES(?, ?)
        """
        CURSOR.execute(sql, (self.company_name, self.location))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, company_name, location):
        publisher = cls(company_name, location)
        publisher.save()
        return publisher
 
    def update(self):
        sql = """
            UPDATE publishers SET company_name = ?, location = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.company_name, self.location, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM publishers WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        pass