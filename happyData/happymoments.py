import csv 
from peewee import *
db = PostgresqlDatabase('happynotes',user='sara',password='sara',host='localhost',port=5432)
import pandas as pd

class BaseModel(Model):
    class Meta:
        database=db

class HappyNote(BaseModel):
    content = TextField()
    category = CharField()
    workerID = IntegerField()

class Worker(BaseModel):
    workerID = IntegerField()
    age = FloatField()
    country = CharField()
    gender = CharField()
    marital = CharField()
    parenthood = CharField()

db.connect()

db.drop_tables([HappyNote])
db.create_tables([HappyNote])

df = pd.read_csv("cleaned_hm.csv")
# haven't tried in range(100) yet
for i in range(100):
    HappyNote(
            content = df['cleaned_hm'][i],
            category = df['predicted_category'][i],
            workerID = df['wid'][i]
        ).save()

db.drop_tables([Worker]) 
db.create_tables([Worker])

df_worker = pd.read_csv("demographic.csv")
for i in range(len(df_worker['wid'])):
    Worker(
        workerID = df_worker['wid'][i],
        age = df_worker['age'][i],
        country = df_worker['country'][i],
        gender = df_worker['gender'][i],
        marital = df_worker['marital'][i],
        parenthood = df_worker['parenthood'][i]
    ).save()

# with open('cleaned_hm.csv', newline='') as f:
#     reader = csv.DictReader(f)
#     rows = []
#     for row in reader:
#         HappyNote(
#             content = row['cleaned_hm'],
#             category = row['predicted_category'],
#             workerID = row['wid']
#         ).save()



