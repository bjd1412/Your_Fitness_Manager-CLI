#lib/publisher.py
from models.__init__ import CURSOR, CONN



class Fitness:
    all = {}

    def __init__(self, training, id=None):
        self.id = id
        self.training = training


    def __repr__(self):
        return f"<Fitness: {self.training}>"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS fitness (
            id INTEGER PRIMARY KEY,
            training TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS fitness;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO fitness (training) VALUES (?)
        """
        CURSOR.execute(sql, (self.training))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, training):
        fitness = cls(training)
        fitness.save()
        return fitness
 
    def update(self):
        sql = """
            UPDATE fitness SET training = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.training, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM fitness WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        fitness = cls.all.get(row[0])

        if fitness:
            fitness.training = row[1]
        else:
            fitness = cls(row[1])
            fitness.id = row[0]
            cls.all[fitness.id] = fitness
        return fitness

    @classmethod
    def find_by_id(cls, id):
        sql = """
        SELECT * FROM fitness WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, training):
        sql = """
            SELECT * FROM fitness WHERE training = ? 
        """
        row = CURSOR.execute(sql, (training,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM fitness
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

           