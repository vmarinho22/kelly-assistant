from peewee import AutoField, CharField, DateField, Model, SqliteDatabase

db_connection = SqliteDatabase('database.db')

class BaseModel(Model):
    class Meta:
        database = db_connection
        

class Event(BaseModel):
    id = AutoField(primary_key=True)
    title = CharField(max_length=255)
    date = DateField()
    
def create_tables(): 
    db_connection.connect()
    db_connection.create_tables([Event], safe=True)
    db_connection.close()