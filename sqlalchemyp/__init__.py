# -*- coding: utf-8 -*-

import importlib

import sqlparse
from sqlalchemy import orm

__all__ = ['print_sql', 'get_sql']


def _get_db_dialect(dialect):
    module_name = 'sqlalchemy.dialects.{}'.format(dialect)
    try:
        dialect = importlib.import_module(module_name)
    except ImportError:
        raise ValueError('Unsupported dialect: {}'.format(dialect))
    return dialect.dialect()


def _get_query_statement(query):
    if isinstance(query, orm.query.Query):
        return query.statement
    else:
        return query


def get_sql(query, dialect):
    statement = _get_query_statement(query)
    db_dialect = _get_db_dialect(dialect)

    sql = statement.compile(
        dialect=db_dialect,
        compile_kwargs={'literal_binds': True}
    )
    return sqlparse.format(str(sql), reindent=True)


def print_sql(query, dialect):
    print('{sql};'.format(sql=get_sql(query, dialect)))
