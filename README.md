# SQLAlchemy Print Query

[![Build Status](https://travis-ci.org/evangilo/sqlalchemyp.svg?branch=master)](https://travis-ci.org/evangilo/sqlalchemyp)
[![PyPI version](https://badge.fury.io/py/sqlalchemyp.svg)](https://badge.fury.io/py/sqlalchemyp)

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
