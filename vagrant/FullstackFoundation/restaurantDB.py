from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from restaurantHelper import turnHtml
from database_setup	import Restaurant

engine = create_engine('sqlite:///restaurantmenu.db')
DBSession = sessionmaker(bind=engine)
session = DBSession()


def getAllRestaurants():

	restaurants = session.query(Restaurant).order_by(Restaurant.name)
	html = ""

	for place in restaurants:
		html += turnHtml(place.name, str(place.id))
	return html

## Add a post to the database.
def addRestaurant(content):
	print "adding " + content + " to list"
	rest1 = Restaurant(name=content)
	session.add(rest1)
	session.commit()
	print "done adding to list"

def editRestaurant(content, idnr):
	print "renaming to " + content
	query = session.query(Restaurant).filter_by(id = idnr).one()
	query.name = content
	session.add(query)
	print "added"
	session.commit()
	print "done renaming"


def deleteRestaurant(idnr):
	print "deleting "
	query = session.query(Restaurant).filter_by(id = idnr).one()
	if query != []:
		session.delete(query)
		print "deleted"
	session.commit()
	print "done deleting"

