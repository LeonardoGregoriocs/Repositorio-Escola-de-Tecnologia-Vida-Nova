from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.sql.sqltypes import DateTime

SQLALCHEMY_DATABASE_URL = "sqlite:///mydatabase.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo = True)
Session = sessionmaker(bind=engine)
session = Session()

class BaseModel(object):
    @declared_attr
    def create_at(cls):
        return Column(DateTime, default= datetime.now())

Base = declarative_base(cls=BaseModel)

class Pessoa(Base): 
    __tablename__ = "pessoas"

    id= Column(Integer,primary_key=True)
    name= Column(String)
    documents= Column(String, unique=True)
    phonenumber= Column(String)


Base.metadata.create_all(engine)

p1 = Pessoa(name="Leonardo", documents="12345678998", phonenumber="19988885565")
p2 = Pessoa(name="Edivane", documents="98765432112", phonenumber="1987541236")
p3 = Pessoa(name="William", documents="2525252525", phonenumber="14985236541")
p4 = Pessoa(name="Thiago", documents="14785236988", phonenumber="1987541236")

session.add(p1)
session.add(p2)
session.add(p3)
session.add(p4)

session.commit()