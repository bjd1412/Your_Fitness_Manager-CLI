#lib/publisher.py
from models.__init__ import CURSOR, CONN



class Fitness:
    all = {}

    def __init__(self, training, target, id=None):
        self.id = id
        self.training = training
        self.target = target


    def __repr__(self):
        return f"<Fitness: {self.training}, {self.target}>"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS fitness (
            id INTEGER PRIMARY KEY,
            training TEXT,
            target TEXT)
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
            INSERT INTO fitness (training, target)
             VALUES (?,?)
        """
        CURSOR.execute(sql, (self.training, self.target))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, training, target):
        fitness = cls(training, target)
        fitness.save()
        return fitness
 
    def update(self):
        sql = """
            UPDATE fitness SET training = ?, target = ?
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
            fitness.target = row[2]
        else:
            fitness = cls(row[1], row[2])
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

           