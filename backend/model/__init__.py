from backend import db

# 创建模型对象


class Country(db.Model):
    __tablename__ = 'COUNTRY'
    id = db.Column('COUNTRY_ID', db.Integer, primary_key=True)
    name = db.Column('COUNTRY_NAME', db.VARCHAR(255))
    img = db.Column('COUNTRY_IMG', db.VARCHAR(255))
    small = db.Column('COUNTRY_SMALL', db.VARCHAR(255))
    des = db.Column('COUNTRY_DES', db.VARCHAR(255))
    contents = db.relationship('Contents', backref='country_content')
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'name': self.name,
            'img': self.img,
            'small': self.small,
            'des': self.des,
        }


class Tags(db.Model):
    __tablename__ = 'TAGS'
    id = db.Column('TAG_ID', db.Integer, primary_key=True)
    name = db.Column('TAG_NAME', db.VARCHAR(255))
    img = db.Column('TAG_IMG', db.VARCHAR(255))
    contents = db.relationship('Contents', backref='tag_content')
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'name': self.name,
            'img': self.img,
        }


class Contents(db.Model):
    __tablename__ = 'CONTENT'
    id = db.Column('CONTENT_ID', db.Integer, primary_key=True)
    content = db.Column('CONTENT', db.VARCHAR(255))
    img = db.Column('CONTENT_IMAGE', db.VARCHAR(255))
    country_id = db.Column(db.Integer, db.ForeignKey('COUNTRY.COUNTRY_ID'))
    tag_id = db.Column(db.Integer, db.ForeignKey('TAGS.TAG_ID'))
    content_name = db.Column('CONTENT_NAME', db.VARCHAR(255))

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'content': self.content,
            'img': self.img,
            'country_id': self.country_id,
            'tag_id': self.tag_id,
            'content_name': self.content_name

        }


class Festival(db.Model):
    __tablename__ = 'FESTIVAL'
    id = db.Column('FESTIVAL_ID', db.Integer, primary_key=True)
    name = db.Column('FESTIVAL_NAME', db.VARCHAR(255))
    date = db.Column('FESTIVAL_DATE', db.DATE)
    tag_id = db.Column('TAG_ID', db.Integer)
    country_id = db.Column('COUNTRY_ID', db.Integer)

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'name': self.name,
            'date': self.date,
            'tag_id': self.tag_id,
            'country_id': self.country_id,
        }


class Events(db.Model):
    __tablename__ = 'EVENT'
    id = db.Column('EVENT_ID', db.Integer, primary_key=True)
    name = db.Column('EVENT_NAME', db.VARCHAR(255))
    day = db.Column('EVENT_DATE', db.DATE)
    des = db.Column('EVENT_DES', db.VARCHAR)
    time = db.Column('EVENT_TIME', db.VARCHAR)
    loc = db.Column('EVENT_LOCATION', db.VARCHAR)
    festival_id = db.Column(db.Integer, db.ForeignKey('FESTIVAL.FESTIVAL_ID'))
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'name': self.name,
            'des': self.des,
            'day': self.day,
            'time': self.time,
            'loc': self.loc,
            'festival_id': self.festival_id,
        }


class Quiz(db.Model):
    __tablename__ = 'QUIZ'
    id = db.Column('QUIZ_ID', db.Integer, primary_key=True)
    img = db.Column('QUIZ_IMG', db.VARCHAR(255))
    answer = db.Column('QUIZ_ANS', db.VARCHAR(255))
    quiz = db.Column('QUIZ', db.VARCHAR(255))
    option = db.Column('QUIZ_OPTION', db.VARCHAR(255))
    date = db.Column('DATE', db.DATE)
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'img': self.img,
            'answer': self.answer,
            'quiz': self.quiz,
            'option': self.option,
            'date': self.date,
        }


class Recipe(db.Model):
    __tablename__ = 'RECIPE'
    id = db.Column('RECIPE_ID', db.Integer, primary_key=True)
    name = db.Column('RECIPE_NAME', db.VARCHAR(255))
    ingredients = db.Column('INGREDIENTS', db.VARCHAR(255))
    procedure = db.Column('PROCEDURE', db.VARCHAR(255))
    pic = db.Column('PIC', db.VARCHAR(255))
    country_id = db.Column(db.Integer, db.ForeignKey('COUNTRY.COUNTRY_ID'))
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'name': self.name,
            'ingredients': self.ingredients,
            'procedure': self.procedure,
            'pic': self.pic,
            'country_id': self.country_id,
        }


class Restaurant(db.Model):
    __tablename__ = 'RESTAURANT'
    id = db.Column('Index', db.Integer, primary_key=True)
    name = db.Column('Name', db.VARCHAR(255))
    address = db.Column('Address', db.VARCHAR(255))
    latitude = db.Column('Latitude', db.VARCHAR(255))
    longitude = db.Column('Longitude', db.VARCHAR(255))
    timings = db.Column('Timings', db.VARCHAR(255))
    price = db.Column('Price', db.Integer)
    rate = db.Column('Rate', db.Float(255))
    country = db.Column('Country', db.VARCHAR(255))

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'timings': self.timings,
            'price': self.price,
            'rate': self.rate,
            'country': self.country,
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
