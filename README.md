# python-cli-note-taker

Project 9 in General Assembly SEI35

To try out my note taker:

1. Make sure you have Python3, pipenv, and PostgreSQL installed!
1. Clone down this repo
1. In the project folder, run `pipenv install`
1. In `notetaker.py`, update your PostgreSQL settings. You may need to add a 'notes' database on your local machine.
1. Then: `pipenv run python3 notetaker.py -h`

The project requirements provied by GA are summarized below:

# Python Command Line Application

To learn Python and SQL, you'll be building a command line application!

## Prerequisites

- Python
- SQL and PeeWee

### Note Taker

Users sould be able to create notes with titles and contents. They should be able to see a list of their notes and select and view a specific note.

# Also in this repo: an API built using Python, SQL, and Flask

To host this API on your local machine, run `pipenv run python3 noteAPI.py`.

The RESTful routes available include:

POST and GET at `/notes/`

POST, GET, PUT, and DELETE at `/notes/<id>` where `<id>` coreesponds to your local database's id number.
