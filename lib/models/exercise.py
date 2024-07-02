# lib/Videogame.py
from models.__init__ import CONN, CURSOR
from models.fitness import Fitness

class Exercise:
    all = {}
    
    def __init__(self, name, reps, fitness_id, id=None):
        self.id = id
        self.name = name
        self.reps = reps
        self.fitness_id = fitness_id

    @property
    def name(self):
        return self._name 

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("name must be a non-empty string")

    @property
    def reps(self):
        return self._reps

    @reps.setter
    def reps(self, reps):
        if isinstance(reps, str) and len(reps):
            self._reps = reps
        else:
            raise ValueError("reps must be a non-empty string")

    def __repr__(self):
        return(
            f"<Exercise: {self.name}, {self.reps}>"
        )

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS exercises(
            id INTEGER PRIMARY KEY,
            name TEXT,
            reps TEXT,
            fitness_id INTEGER,
            FOREIGN KEY (fitness_id) REFERENCES fitness(id))
            """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """
        DROP TABLE IF EXISTS exercises;
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        sql = """
            INSERT INTO exercises( name, reps, fitness_id)
            VALUES (?, ?, ?)
            """
        CURSOR.execute(sql, (self.name, self.reps, self.fitness_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, reps, fitness_id):
        exercise = cls( name, reps, fitness_id)
        exercise.save()
        return exercise

    def update(self):
        sql = """
            UPDATE exercises SET  name = ?, reps = ?, fitness_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.reps, self.fitness_id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM exercises WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        exercise = cls.all.get(row[0])

        if exercise:
            exercise.name = row[1]
            exercise.reps = row[2]
            exercise.fitness_id = row[3]
        else:
            exercise = cls(row[1], row[2], row[3])
            exercise.id = row[0]
            cls.all[exercise.id] = exercise
        return exercise

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM exercises WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT * FROM exercises WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM exercises
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_all_by_id(cls, fitness_id):
        sql = """
            SELECT * FROM exercises WHERE fitness_id = ?
        """
        rows = CURSOR.execute(sql, (fitness_id,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]









            
        