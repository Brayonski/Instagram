Instagram
===================

- - - -
Author: [Brian Mutai](https://github.com/Brayonski/Instagram)
## Description
[Vyaktigat Gailaree](https://the-snaps.herokuapp.com/) This web app is used to show pictures based on different location of shooting,categories and has photo descriptions. 

------------------------------------------------------------------------

## User 

1. View photos of interest
2. Click on a single photo to expand it and also view the details of the photo which is description and category.
3. Copy link of the photo to share

## Features

+ [x] List photos of all categories
+ [x] show category of an image
+ [x] Images have desciption
+ [x] Categorize pictures
+ [x] search image according to category
+ [x] filter images by category
+ [x] filter images by location



## Installation

### Requirements
This project was created on a debian linux platform but should work on other unix based[not limited to] sytems.
* Tested on Debian Linux
* Python 3.6.4

### Cloning the repository
```bash
git clone https://github.com/Brayonski/Instagram && cd Instagram
```

### Creating a virtual environment
```bash
sudo apt-get install python3.6-venv
python3.6 -m venv virtual
source virtual/bin/activate
```

### Installing dependencies
```bash
pip3 install -r requirements
```
The following libraries are required

```bash
config==0.4.0
dj-database-url==0.5.0
Django==1.11
django-bootstrap3==11.0.0
django-heroku==0.3.1
gunicorn==19.9.0
Pillow==5.2.0
psycopg2==2.7.5
psycopg2-binary==2.7.5
python-decouple==3.1
pytz==2018.5
whitenoise==4.1
```


### Running Tests
```bash
python3 manage.py test
```

### Running the web app in development
```bash
python3 manage.py runserver
```
Open the app on your browser, by default on `127.0.0.1:8000`

## Live Demo

https://the-snaps.herokuapp.com/


## Quickstart

```
usage: manage.py [-?] {server,test,shell,runserver} ...

positional arguments:
  {server,test,shell,runserver}
    server              Runs the Flask development server i.e. app.run()
    test                Run the unit tests.
    shell               Runs a Python shell inside Flask application context.
    runserver           Runs the Flask development server i.e. app.run()

optional arguments:
  -?, --help            show this help message and exit
```

## Technology used

* [Python3.6](https://www.python.org/)
* [Django1.11](https://www.djangoproject.com/)
* [Flask](http://flask.pocoo.org/)
* [Heroku](https://heroku.com)

## Contributing

- Git clone [https://github.com/Brayonski/Instagram]
- Write your tests on `tests/`
- If everything is OK. push your changes and make a pull request. ;)

## License ([MIT License](http://choosealicense.com/licenses/mit/))

This project is licensed under the MIT Open Source license, (c) [Brian Mutai](https://github.com/Brayonski/Instagram)