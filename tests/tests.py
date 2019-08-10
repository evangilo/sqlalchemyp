import unittest

from sqlalchemy import create_engine, Column, types, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemyp import get_sql

Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    id = Column(types.Integer, primary_key=True)
    name = Column(types.String(250), nullable=False)


class TestSQLAlchemyPrintQuery(unittest.TestCase):
    def test_get_sql(self):
        p = Person.__table__
        query = select([p.c.id, p.c.name])
        self.assertEquals('SELECT person.id,\n       person.name\nFROM person',
                          get_sql(query, 'sqlite'))

    def test_get_sql_using_orm_query(self):
        DBSession = sessionmaker(bind=create_engine('sqlite://'))
        session = DBSession()

        query = session.query(Person)
        self.assertEquals('SELECT person.id,\n       person.name\nFROM person',
                          get_sql(query, 'sqlite'))

    def test_invalid_dialect(self):
        with self.assertRaises(ValueError):
            get_sql(None, 'sqlite2')

    def test_postgresql_as_default_dialect(self):
        p = Person.__table__
        query = select([p.c.id, p.c.name])
        self.assertEquals('SELECT person.id,\n       person.name\nFROM person',
                          get_sql(query))


if __name__ == '__main__':
    unittest.main()
