import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    """ Connect to the application's configured database. The connection
    is unique for each request (since the g object is unique for each request)
    and will be reused if this is called again in the same request."""
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        # Return rows that behave like dicts. This allows accessing the columns by name.
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    """ If this request connected to the database, close the
        connection.
    """
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    """Clear existing data and create new tables."""
    db = get_db()

    # open_resource() opens a file relative to the flaskr package, which is useful since you won’t necessarily know
    # where that location is when deploying the application later.
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')  # defines a command line command called init-db that calls the init_db function and shows a
# success message to the user.
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Initialized')


def init_app(app):
    """This should be called from the application factory function to register the functions once the app instance
    is available so that it uses them. """
    app.teardown_appcontext(close_db)  # it will call close_db when the app context is popped
    app.cli.add_command(init_db_command)
