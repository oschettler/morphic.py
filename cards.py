'''
'''
import datetime
import morphic
from peewee import *

db = SqliteDatabase('cards.db', pragmas={'foreign_keys': 1})
class BaseModel(Model):
    class Meta:
        database = db

class Card(BaseModel, morphic.Text):
    title = CharField()
    body = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    def __init__(self, world):
        BaseModel.__init__(self)
        morphic.Text.__init__(
            self, world,
            "Ich bin ein Text"
        )


class Board(morphic.World):
    def context_menu(self):
        if self.is_dev_mode:
            menu = super().context_menu()
        else:
            menu = morphic.Menu(self, self.__class__.__name__)
            menu.add_item("create a card...", 'create_card')
            menu.add_item("switch to dev mode", 'toggle_dev_mode')
        return menu

    
    def create_card(self):
        card = Card(self).pick_up()


def run():
    board = Board()
    board.toggle_dev_mode()
    board.loop()


if __name__ == '__main__':
    run()