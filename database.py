from app import  db

print("start to create model")
class user(db.Model):  # 继承SQLAlchemy.Model对象，一个对象代表了一张表
    #__table_args__ = {"useexisting": True}
    _id= db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)  # id 整型，主键，自增，唯一
    _account = db.Column(db.String(20),unique=True)
    _passwd = db.Column(db.String(20))
    _email = db.Column(db.String(20))
    __tablename__ = 'user'  # 该参数可选，不设置会默认的设置表名，如果设置会覆盖默认的表名

    def __init__(self,  acount,passwd,email):  # 初始化方法，可以对对象进行创建
        self._account = acount
        self._passwd = passwd
        self._email = email
    def __repr__(self):  # 输出方法，与__str__类似，但是能够重现它所代表的对象
        return '<user %r, %r, %r>' % (self._id, self._account, self._passwd)


class paper(db.Model):  # 继承SQLAlchemy.Model对象，一个对象代表了一张表
    #__table_args__ = {"useexisting": True}
    _id= db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)  # id 整型，主键，自增，唯一
    _title = db.Column(db.String(100))
    _abstract = db.Column(db.String(20000))
    _content = db.Column(db.TEXT(200000))
    _author = db.Column(db.String(20),default="null")
    _catlog = db.Column(db.String(20))
    _numOfnotes = db.Column(db.Integer,default = 0)

    __tablename__ = 'paper'  # 该参数可选，不设置会默认的设置表名，如果设置会覆盖默认的表名
    def __init__(self, title, abstract,content = '',author = '' ,catlog = ''):  # 初始化方法，可以对对象进行创建
        self._title = title
        self._abstract =abstract
        self._content = content
        self._author = author
        self._catlog = catlog

    def __repr__(self):  # 输出方法，与__str__类似，但是能够重现它所代表的对象
        return '<paper %r, %r, %r>' % (self._title, self._abstract, self._author)


class test(db.Model):  # 继承SQLAlchemy.Model对象，一个对象代表了一张表
    # __table_args__ = {"useexisting": True}
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)  # id 整型，主键，自增，唯一
    _testdata = db.Column(db.String(20))
    __tablename__ = 'test'

    def __init__(self,testdata):  # 初始化方法，可以对对象进行创建
        self._testdata = testdata

    def __repr__(self):  # 输出方法，与__str__类似，但是能够重现它所代表的对象
        return '<test %r, %r, %r>' % (self.s_id, self.s_name, self.sage)