from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Categories(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    post = db.relationship('Post', backref='category', lazy=True)

    def __str__(self):
        return f"{self.name}"

    @classmethod
    def get_all_categories(cls):
        return cls.query.all()
    
 


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100))
    body = db.Column(db.String(100), unique=True, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey(
        'categories.id'), nullable=True)

    def __str__(self):
        return f"{self.title}"


    @classmethod
    def get_all_posts(cls):
        return cls.query.all()

    def delete_object(self):
        db.session.delete(self)
        db.session.commit()
        return True

    @classmethod
    def create_post(cls ,post_data):
        post = cls(**post_data)
        db.session.add(post)
        db.session.commit()
        return post

    @classmethod
    def get_specific_posts(cls, id):
        return cls.query.get(id)



    def update_posts(self, updated_data):
        self.title = updated_data["title"]
        self.body = updated_data["body"]
        db.session.add(self)
        db.session.commit()
        return True