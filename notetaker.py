import argparse
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

parser = argparse.ArgumentParser(description="add notes to PostgreSQL database")
parser.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("action", help="what action you'd like to take", choices=['list','create'],default='list',)
args = parser.parse_args()

user_action = args.action

if user_action=='list':
    print("now showing: your notes!")
    note_list = Note.select()
    if args.quiet:
        print('the short list')
        for single_note in list(note_list):
            print(single_note.title," ",single_note.date)
    else:
        print('the long list')
        for single_note in list(note_list):
            print(f"""{single_note.title} {single_note.date}
    {single_note.content}""")
elif user_action=='create':
    title = input('Please provide the title of your new note: ')
    content = input('Please provide the content: ')
    Note(title=title,date=time.ctime(),content=content).save()
    print(f"""Note saved! 
Title: {title}
Content: {content}    
    """)
