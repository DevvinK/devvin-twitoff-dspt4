TODO: instructions for git clone

## Setup

TODO: instructions for virtual environment

Also setup a database:

'''sh
# Windows: make sure there isn't a space between the = sign or else errors will be thrown
# Windows users can omit the "FLASK_APP=web_app" part after initializing the first time

FLASK_APP=web_app flask db init 

# Needs to be reran everytime db is changed
FLASK_APP=web_app flask db migrate 
FLASK_APP=web_app flask db upgrade 
'''

## Usage 

'''sh
# Mac:
FLASK_APP=hello.py flask run

# Windows: make sure there isn't a space between the = sign or else errors will be thrown
set FLASK_APP=hellp.py # one-time thing, to set the env var 
flask run
'''