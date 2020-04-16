from Admin.BASE import *


app,db = create_app()
class Plants(db.Model):
    __tablename__ = 'test_plants'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(24), unique=True)
    body = db.Column(db.String(5000))

# db.create_all()# 要先创建表，不然会提示找不到表

    @staticmethod
    def plants_add(name,body):
        user = Plants()
        user.name = name
        user.body = body
        db.session.add(user)
        db.session.commit()


class Photo(db.Model):
    __tablename__ = 'test_photo'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(24))
    path = db.Column(db.String(100))

# db.create_all()# 要先创建表，不然会提示找不到表

    @staticmethod
    def photo_add(name,path):
        user = Photo()
        user.name = name
        user.path = path
        db.session.add(user)
        db.session.commit()

class Ritui(db.Model):
    __tablename__ = 'test_ritui'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(24))
    study_name = db.Column(db.String(50))
    put_plants = db.Column(db.String(100))
    min_knowledge = db.Column(db.String(1000))

    @staticmethod
    def ritui_add(name, study_name, put_plants, min_knowledge):
        user = Ritui()
        user.name = name
        user.study_name = study_name
        user.put_plants = put_plants
        user.min_knowledge = min_knowledge
        db.session.add(user)
        db.session.commit()
