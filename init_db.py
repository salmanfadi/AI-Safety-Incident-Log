from app import app, db
from app.utils import populate_sample_data

with app.app_context():
    db.create_all()

    populate_sample_data()
    
    print("Database setup complete!")