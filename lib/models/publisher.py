#lib/publisher.py
from models.__init__ import CURSOR, CONN



class Publisher:
    all = {}

    def __init__(self, company_name, location, id=None):
        self.id = id
        self.company_name = company_name
        self.location = location

    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        if isinstance(company_name, str) and len(company_name):
            self._company_name = company_name
        else:
            raise ValueError("Company name must be a non-empty string")

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        if isinstance(location, str) and len(location) > 5:
            self._location = location
        else:
            raise ValueError("Location must be a non-empty string with more than 5 characters.")



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
        publisher = cls.all.get(row[0])

        if publisher:
            publisher.company_name = row[1]
            publisher.location = row[2]
        else:
            publisher = cls(row[1], row[2])
            publisher.id = row[0]
            cls.all[publisher.id] = publisher
        return publisher

    @classmethod
    def find_by_id(cls, id):
        sql = """
        SELECT * FROM publishers WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, company_name):
        sql = """
            SELECT * FROM publishers WHERE company_name = ? 
        """
        row = CURSOR.execute(sql, (company_name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM publishers
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

           