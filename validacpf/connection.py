from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine(f'mysql+pymysql://{"root"}:{""}@{"localhost"}:{"3306"}/{"cpf"})

Base = declarative_base()

Session = sessionmaker(bind=engine)

session = Session()
