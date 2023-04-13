from datetime import datetime
from settings import DatabaseSettings

import peewee as pw
db_set = DatabaseSettings()

# db = pw.SqliteDatabase('lecture.db')
db = pw.SqliteDatabase(db_set.db_name)

class ModelBase(pw.Model):
    created_at = pw.DateTimeField(default=datetime.now().strftime("%Y-%m-%d - %H:%M:%S"))

    class Meta():
        database = db


class History(ModelBase):
    numbers = pw.TextField()
    message = pw.TextField()