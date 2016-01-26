from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pups import Base, Shelter, Puppy
from datetime import timedelta, date

engine = create_engine('sqlite:///puppyshelter.db')
DBSession = sessionmaker(bind=engine)
session = DBSession()
pups = session.query(Puppy).order_by(Puppy.name)
for puppy in pups:
	print puppy.name + ", " + puppy.gender

halfYear = date.today() - timedelta(days=182)
pups = session.query(Puppy).filter(Puppy.dateOfBirth > halfYear ).order_by(Puppy.dateOfBirth.desc())
for puppy in pups:
	print puppy.name +", "+ puppy.dateOfBirth.__str__()

pups = session.query(Puppy).order_by(Puppy.weight)
for puppy in pups:
	print puppy.name + ", " + puppy.weight.__str__() +"lbs"

pups = session.query(Puppy).order_by(Puppy.shelter_id)
for puppy in pups:
	print puppy.name + ", " + puppy.shelter_id.__str__()