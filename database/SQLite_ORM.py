from peewee import SqliteDatabase, Model, CharField, IntegerField

# подключаемся к базе данных my_database.db
db = SqliteDatabase("users_data.db")


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    user_id = IntegerField(primary_key=True)
    username = CharField()
    first_name = CharField()
    last_name = CharField(null=True)
    lon = IntegerField()
    lat = IntegerField()


def create_models():
    db.create_tables(BaseModel.__subclasses__())
