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
parser.add_argument("-u")
parser.add_argument("action", help="what action you'd like to take", choices=['list','create','clear-all'],default='list',)
args = parser.parse_args()

user_action = args.action

if user_action=='list':
    note_list = Note.select()
    print()
    if args.quiet:
        for single_note in list(note_list):
            print(single_note.title," ",single_note.date,"\n")
        search_title = input('Would you like to view a single note? \nPlease type the title here, or hit enter to exit: ')
        if search_title != "":
            single_note = Note.get(Note.title == search_title)
            print(f"""
    {single_note.title} {single_note.date}
        {single_note.content}
    """)


    else:
        for single_note in list(note_list):
            print(f"""
{single_note.title} {single_note.date}
    {single_note.content}
""")
elif user_action=='create':
    title = input('Please provide the title of your new note: ')
    content = input('Please provide the content: ')
    Note(title=title,date=time.ctime(),content=content).save()
    print(f"""Note saved! 
Title: {title}
Content: {content}    
    """)
elif user_action=='clear-all':
    db.drop_tables([Note])
    db.create_tables([Note])