from init import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(32), unique=False)
    phone = db.Column(db.String(32), unique=True)
    email = db.Column(db.String(32), unique=True)
    token = db.Column(db.String(32), unique=True)


class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(), unique=False)
    category = db.Column(db.String(), unique=False)
    datetime = db.Column(db.DateTime(), unique=False)
    from_id = None
    to_id = None
    is_read = db.Column(db.Boolean(), unique=False)


class Tags(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=False)


tags_users = None
'''db.Table('tags',
                      db.Column('tag_id', db.Integer, db.ForeignKey('tag.id', ondelete='CASCADE')),
                      db.Column('post_id', db.Integer, db.ForeignKey('post.id', ondelete='CASCADE')),
                      db.PrimaryKeyConstraint('tag_id', 'post_id')
                      )'''
# все неопределенные поля это заглушки
