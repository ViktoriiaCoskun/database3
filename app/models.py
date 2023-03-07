from . import db

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    imageLink = db.Column(db.String(100), nullable=False)
    language = db.Column(db.String(100), nullable=False)
    pages = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    link = db.Column(db.String(100), nullable=False)
    year = db.Column(db.String(100), nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'author': self.author,
            'country': self.country,
            'imageLink': self.imageLink,
            'language': self.language,
            'pages': self.pages,
            'title': self.title,
            'link': self.link,
            'year': self.year
        }    

