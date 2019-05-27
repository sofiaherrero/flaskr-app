## Flaskr with custom additions
Flaskr blog app from the the [Flask tutorial](http://flask.pocoo.org/docs/1.0/tutorial/) with custom additions.

### Install and run

Create a virtualenv and activate it:

    $ python3 -m venv venv
    $ . venv/bin/activate

Install Flaskr (run this command from inside the directory flaskr-app where the setup.py file is):

    $ pip install -e .

Then:

    $ export FLASK_APP=flaskr
    $ export FLASK_ENV=development
    $ flask init-db
    $ flask run

and open <http://127.0.0.1:5000> in a browser.

### Using Docker

Instead of installing and running it, you can create an image and run it in a Docker container using the Dockerfile. Create the image with:

``` $ docker build -t flaskr-app . ```

and run it with:

``` docker run -p 5000:5000 flaskr-app ```

then open <http://localhost:5000> in a browser


## Test

    $ pip install '.[test]'
    $ pytest

Run with coverage report:

    $ coverage run -m pytest
    $ coverage report
    $ coverage html  # open htmlcov/index.html in a browser
