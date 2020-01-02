from flask_sqlalchemy import SQLAlchemy
from core import app


db = SQLAlchemy(app)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))

    def __repr__(self):
        return f"Person <{self.name} {self.last_name}>"

    @classmethod
    def create(self, name, last_name, age):
        person = self(name=name, age=age, last_name=last_name)
        db.session.add(person)
        db.session.commit()
        return person

    @classmethod
    def delete(self, id):
        person = self.query.filter_by(id=id).first()
        if person:
            db.session.delete(person)
            db.session.commit()
            return person
