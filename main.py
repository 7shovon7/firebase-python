import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate('firebase_creds.json')
firebase_admin.initialize_app(cred)

db = firestore.client()


db.collection(u'locations').document(u'location1').set({
    u'city': u'Washington',
    u'state': u'District of Columbia'
})

# db.collection(u'locations').document(u'location1').delete()

# cities = db.collection(u'locations').stream()

# for city in cities:
#     print(f'{city.id} => {city.to_dict()}')
