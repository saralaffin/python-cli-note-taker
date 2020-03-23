from flask import Flask, jsonify, request
from datetime import date
import time
from peewee import *
from playhouse.shortcuts import dict_to_model, model_to_dict

db = PostgresqlDatabase('notes',user='sara',password='sara',host='localhost',port=5432)

class BaseModel(Model):
    class Meta:
        database = db
class Note(BaseModel):
    title= CharField()
    date= DateField()
    content= CharField()

db.connect()

app = Flask(__name__)

@app.route('/notes/',methods=['POST'])
def create_note():
    user_data = request.get_json()
    user_data['date'] = time.ctime()
    new_note = dict_to_model(Note, user_data)
    new_note.save()
    return jsonify({"success":True})

@app.route('/notes/', methods=['GET'])
@app.route('/notes/<id>',methods=['GET','PUT','DELETE'])
def get_note(id=None):
    if id:
        verb = request.method
        if verb == 'GET':
            return jsonify(
                model_to_dict(
                    Note.get(Note.id == id)
                )
            )

        elif verb == 'DELETE':
            Note.delete_by_id(id)
            return jsonify({"success":True})

        else:
            note_to_update = Note.get(Note.id == id)
            if 'content' in request.json:
                note_to_update.content = f"(updated on :{time.ctime()}) {request.json['content']}"
            if 'title' in request.json:
                note_to_update.title = request.json['title']

            note_to_update.save()
            return jsonify({"success":True})

    else:
        notes = []
        for note in Note.select():
            notes.append(model_to_dict(note))
        return jsonify(notes)

app.run(debug=True)