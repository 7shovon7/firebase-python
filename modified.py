import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate('firebase_creds.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

# FUNCTION FOR ADDING DATA TO LOCATIONS COLLECTION


def add_data(doc, city, state):
    db.collection(u'locations').document(u'{}'.format(doc)).set({
        u'city': u'{}'.format(city),
        u'state': u'{}'.format(state)
    })


# ADD DATA USING THAT FUNCTION
add_data('location1', 'Miami', 'Florida')
add_data('location2', 'Denver', 'Colorado')

# READ DATA
cities = db.collection(u'locations').stream()
for city in cities:
    print(f'{city.id} => {city.to_dict()}')

# DELETE DATA
db.collection(u'locations').document(u'location1').delete()

# AGAIN CHECK THE DATA AFTER DELETION
cities = db.collection(u'locations').stream()
for city in cities:
    print(f'{city.id} => {city.to_dict()}')

# TO UPDATE DATA JUST USE THE add_data() FUNCTION AND TRY TO OVERRIDE THE OLD DATA
