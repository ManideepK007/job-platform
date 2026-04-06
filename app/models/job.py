from app import db

class Job(db.Model):
    __tablename__ = "jobs"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    location = db.Column(db.String(100))
    salary = db.Column(db.String(50))