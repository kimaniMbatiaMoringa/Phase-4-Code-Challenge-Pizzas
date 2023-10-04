from app import app
from models import db, Restaurant

restaurants=[
    {   "id": 1,
        "name": "Sottocasa NYC",
        "address": "298 Atlantic Ave, Brooklyn, NY 11201"
  },
  {
        "id": 2,
        "name": "PizzArte",
        "address": "69 W 55th St, New York, NY 10019"
  }
]

with app.app_context():
    Restaurant.query.delete()

    for item in restaurants:
        i = Restaurant(name=item.name, address=item.address)

    db.session.commit()

print("Seeding completed")        