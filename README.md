# SQLAlchemy Print Query

# Install
`pip install git+https://github.com/evangilo/sqlalchemyp#egg=sqlalchemyp`

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
