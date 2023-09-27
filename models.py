"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy
import datetime
db = SQLAlchemy()

def connect_db(app):
    db.init_app(app)    
    
class Cupcake(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    flavor = db.Column(db.String, nullable=False)
    size = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=True, default="https://tinyurl.com/demo-cupcake")
    rating = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Serialize cupcake to a dict of cupcake info."""

        return {
            "id": self.id,
            "flavor": self.flavor,
            "rating": self.rating,
            "size": self.size,
            "image": self.image,
        }

    
