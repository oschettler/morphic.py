'''
'''
import datetime
import morphic
from peewee import *

db = SqliteDatabase('cards.db', pragmas={'foreign_keys': 1})
class BaseModel(Model):
    class Meta:
        database = db

class Card(BaseModel):
    parent = ForeignKeyField('self', backref='children')
    name = CharField()
    body = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)


def run():
    world = morphic.World()
    #m = morphic.Morph()
    #m.pick_up(world)
    world.loop()


if __name__ == '__main__':
    run()