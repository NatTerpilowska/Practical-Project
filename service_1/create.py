from app import db
from app.models import Characters

db.drop_all()
db.create_all()
db.session.commit()