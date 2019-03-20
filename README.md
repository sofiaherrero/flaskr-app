## Flaskr with custom additions
Flaskr blog app from the the [Flask tutorial](http://flask.pocoo.org/docs/1.0/tutorial/) with custom additions.

### Install

Create a virtualenv and activate it:

    $ python3 -m venv venv
    $ . venv/bin/activate

Or on Windows cmd:

    $ py -3 -m venv venv
    $ venv\Scripts\activate.bat

Install Flaskr (run this command from inside the directory flaskr-app where the setup.py file is):

    $ pip install -e .

## Run

    $ p
    $ export FLASK_ENV=development
    $ flask init-db
    $ flask run

Or on Windows cmd:

    > set FLASK_APP=flaskr
    > set FLASK_ENV=development
    > flask init-db
    > flask run

Open <http://127.0.0.1:5000> in a browser.

## Test

    $ pip install '.[test]'
    $ pytest

Run with coverage report:

    $ coverage run -m pytest
    $ coverage report
    $ coverage html  # open htmlcov/index.html in a browser
