from peewee import SqliteDatabase, Model, CharField, IntegerField, FloatField

# подключаемся к базе данных my_database.db
db = SqliteDatabase("users_data.db")


class BaseModel(Model):
    """
    Базовый класс моделей
    """
    class Meta:
        database = db


class User(BaseModel):
    """
    Модель пользователя
    """
    user_id = IntegerField(primary_key=True)
    username = CharField()
    first_name = CharField()
    last_name = CharField(null=True)
    lon = FloatField()
    lat = FloatField()
    history = CharField(null=True)


def create_models() -> None:
    """
    Функция создания моделей
    :return: None
    """
    db.create_tables(BaseModel.__subclasses__())
