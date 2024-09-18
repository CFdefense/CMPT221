"""professor.py: create a table named professors in the marist database"""
from db.db import db

class Professor(db.Model):
    __tablename__ = 'Professors'
    ProfessorID = db.Column(db.Integer,primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(40))
    last_name = db.Column(db.String(40))
    email_address = db.Column(db.String(40))

    # create relationship with courses table. assoc table name = ProfessorCourse
    course = db.relationship('Courses', secondary = 'ProfessorCourse', back_populates = 'Professors')
    def __init__(self):
        self.first_name = self.first_name
        self.last_name = self.last_name
        self.email_address = self.email_address
        pass

    def __repr__(self):
        # add text to the f-string
        return f"""
            "FIRST NAME: {self.first_name},
            LAST NAME: {self.last_name},
            EMAIL ADDRESS: {self.email_address}
        """
    
    def __repr__(self):
        return self.__repr__()