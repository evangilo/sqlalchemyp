# SQLAlchemy Print Query

[![Build Status](https://travis-ci.org/evangilo/sqlalchemyp.svg?branch=master)](https://travis-ci.org/evangilo/sqlalchemyp)
[![PyPI version](https://img.shields.io/pypi/v/sqlalchemyp.svg)](https://pypi.python.org/pypi/sqlalchemyp)
[![PyPI downloads](https://img.shields.io/pypi/dm/sqlalchemyp.svg)](https://pypi.python.org/pypi/sqlalchemyp)

# Install
`pip install sqlalchemyp`

# Usage

```
>>> from sqlalchemyp import print_sql
>>> print_sql(DBSession.query(Hero).filter_by(name='Spider-Man'), 'postgresql')
SELECT hero.id,
       hero.name
FROM hero
WHERE hero.name = 'Spider-Man';
>>>
```
