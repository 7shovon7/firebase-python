
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("firebase_creds.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

#! CREATE AND UPDATE

city1 = {
    u'city': 'Chicago',
    u'state': 'Illinois'
}

city2 = {
    u'city': 'Boston',
    u'state': 'Massachusetts'
}

city3 = {
    u'city': 'Denver',
    u'state': 'Colorado'
}

db.collection(u'cities').document(u'city1').set(city1)
# db.collection(u'cities').document().set(city3)


#! READ

cities_ref = db.collection(u'cities').stream()

for city in cities_ref:
    print(city.to_dict())


#! DELETE

cities_ref = db.collection(u'cities')
cities_ref.document(u'city1').delete()

#! VIEW UPDATED DATA
cities_ref = db.collection(u'cities').stream()

for city in cities_ref:
    print(city.to_dict())
