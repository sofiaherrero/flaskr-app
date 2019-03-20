import os
import tempfile

import pytest
from flaskr import create_app
from flaskr.db import get_db, init_db

with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')


@pytest.fixture
def app():
    """ Call the factory and pass test_config to configure the application and database for testing instead of using
    your local development configuration."""

    db_fd, db_path = tempfile.mkstemp()

    app = create_app({
        'TESTING': True,
        'DATABASE': db_path

    })

    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)

    yield app

    # mkstemp() is a low-level fn, it requires manual cleanup so once returned from the yield
    # (which it will be when the test is run) we do:
    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    """Tests will use the client to make requests to the application without running the server"""
    return app.test_client()


@pytest.fixture
def runner(app):
    """Creates a runner that can call the Click commands registered with the application."""
    return app.test_cli_runner()


class AuthActions(object):
    """
    Class with functions with a client login and logout
    """
    def __init__(self, client):
        self._client = client

    def login(self, username='test', password='test'):
        return self._client.post(
            '/auth/login',
            data={'username': username, 'password': password}
        )

    def logout(self):
        return self._client.get('/auth/logout')


@pytest.fixture
def auth(client):
    return AuthActions(client)
