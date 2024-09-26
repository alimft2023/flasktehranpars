import sqlalchemy as sa
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class Student(Base):
    __tablename__ = "Student"
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255), nullable=False)
    email = sa.Column(sa.String(255), nullable=False)


engine = sa.create_engine("sqlite:///mft.db")
Base.metadata.create_all(engine)

Sessionmaker = sessionmaker(bind=engine)
session = Sessionmaker()
