# digital-beercrate
Digital Beercrate to drink with friends to enjoy drinking together, reach a certain donation goal or just keep track of the amount.


## Installation

1. Clone this Git Repository
2. Create an Virtual Environment with
````
virtualenv -p /bin/python3 .venv
````
3. Adjust Django Settings. (E.g. change database type or enable production mode, etc.)
5. Activate Virtual Environment with
````
. .venv/bin/activate
````
6. Install Requirements with
````
pip install -r requirements
````
4. Apply migration with
````
python3 manage.py migrate
````
5. Create Superuser with
````
python3 manage.py createsuperuser
````
6. Start Server
````
python3 manage.py runserver
````

You should now be able to access the digital beercrate via http://localhost:8000

## Limitations and Adjustment
You may adjust the graphics and gifs in the folder `digitalbeercrate/static` with ones fitting for you.

Also don't forget to create 2 donation goals in the configuration! Therefore:

1. Start the server
2. Login with your superuser
3. Open the configuration panel
4. Create new donation goal

**Note**: By now only 2(!) donation goals are supported!

## Sources
Sources I used:
- Django Framework
- Django Crispy Forms
- Bootstrap
- Jquery Confetti (https://www.jqueryscript.net/animation/Confetti-Animation-jQuery-Canvas-Confetti-js.html)
- Bootle Sound (https://www.youtube.com/watch?v=QdkHUxViWdc)

## Issues and Contact
If you have problems or find a bug, please open an Issue!

Feel free to show me your implementation. Just send me a mail (jonny@riotcat.org) or write me on Matrix (#jonny:matrix.riotcat.org)