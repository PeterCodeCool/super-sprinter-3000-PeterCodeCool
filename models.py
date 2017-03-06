from peewee import *


class ConnectDatabase:
    db = None

    @classmethod
    def get_db(cls):
        if cls.db is None:
            cls.connect_database()
        return cls.db

    @classmethod
    def connect_database(cls):
        with open('connection_info.txt', "r") as f:
            db_details = f.readlines()
            cls.db = PostgresqlDatabase(db_details[0].strip('\n'), user=db_details[1])


class BaseModel(Model):
   class Meta:
        database = ConnectDatabase.get_db()


class Entries(BaseModel):
    story_title = CharField()
    user_story = CharField()
    acceptance_criteria = CharField()
    business_value = IntegerField()
    estimation = FloatField()
    status = CharField()

ConnectDatabase.get_db()
ConnectDatabase.get_db().drop_tables([Entries], safe=True)
ConnectDatabase.get_db().create_tables([Entries], safe=True)
