from peewee import *
from datetime import date
import time

db = PostgresqlDatabase('notes',user='sara',password='sara',host='localhost',port=5432)

class BaseModel(Model):
    class Meta:
        database = db
class Note(BaseModel):
    title= CharField()
    date= DateField()
    content= CharField()

db.connect()
db.drop_tables([Note])
db.create_tables([Note])

Note(title='Trying',date=time.ctime(),content='Lets hope debugging is smooth').save()