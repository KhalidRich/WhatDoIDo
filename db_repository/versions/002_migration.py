from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
event = Table('event', post_meta,
    Column('_id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=150)),
    Column('hosted_by', Integer),
    Column('desc', String(length=2000)),
    Column('time_start', String(length=5)),
    Column('time_end', String(length=5)),
    Column('date', String(length=11)),
)

user = Table('user', post_meta,
    Column('_id', Integer, primary_key=True, nullable=False),
    Column('email', String(length=120)),
    Column('fname', String(length=25)),
    Column('lname', String(length=25)),
    Column('school', String(length=25)),
    Column('sex', SmallInteger),
    Column('role', SmallInteger, default=ColumnDefault(0)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['event'].create()
    post_meta.tables['user'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['event'].drop()
    post_meta.tables['user'].drop()
