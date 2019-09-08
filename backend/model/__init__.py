from backend import db

# 创建模型对象


class Country(db.Model):
    __tablename__ = 'COUNTRY'
    id = db.Column('COUNTRY_ID', db.Integer, primary_key=True)
    name = db.Column('COUNTRY_NAME', db.VARCHAR(255))
    contents = db.relationship('Contents', backref='country_content')
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'name': self.name,
        }

    def __repr__(self):
        return '<Country %s>' % self.name


class Tags(db.Model):
    __tablename__ = 'TAGS'
    id = db.Column('TAG_ID', db.Integer, primary_key=True)
    name = db.Column('TAG_NAME', db.VARCHAR(255))
    contents = db.relationship('Contents', backref='tag_content')
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'name': self.name,

        }


class Contents(db.Model):
    __tablename__ = 'CONTENT'
    id = db.Column('CONTENT_ID', db.Integer, primary_key=True)
    content = db.Column('CONTENT', db.VARCHAR(255))
    country_id = db.Column(db.Integer, db.ForeignKey('COUNTRY.COUNTRY_ID'))
    tag_id = db.Column(db.Integer, db.ForeignKey('TAGS.TAG_ID'))
    #country = db.relationship('Country', backref='contents')

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'content': self.content,
            'country_id': self.country_id,
            'tag_id': self.tag_id
        }


# 1.创建表
db.create_all()

# 2.增加记录
# admin = Tags(id='15', name='ddd')

# guest = User(username='guest', email='guest@example.com')
# db.session.add(admin)
# db.session.add(guest)
# db.session.commit()

# 3.查询记录,注意查询返回对象，如果查询不到返回None
if __name__ == '__main__':
    # country = Country.query.filter(Country.name == "India")  # 查询所有
    content = Contents.query.all()
    # Tags.query.filter_by(username='admin').first()  # 条件查询
    # Tags.query.order_by(User.username).all()  # 排序查询
    # Tags.query.limit(1).all()  # 查询1条
    # Tags.query.get(id=123)  # 精确查询
    # print(country[0].name)

    print(content[0].country.name)
