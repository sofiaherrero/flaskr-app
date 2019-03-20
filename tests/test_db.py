import sqlite3

import pytest
from flaskr.db import get_db


def test_get_close_db(app):
    """ Same connection should be returned every time get_db is called."""
    with app.app_context():
        db = get_db()
        assert db is get_db()

    with pytest.raises(sqlite3.ProgrammingError) as e:
        db.execute('SELECT 1')

    print('e is {e}')
    assert 'closed' in str(e)


def test_init_db_command(runner, monkeypatch):
    """ monkeypatch fixture is used to replace the init_db function with one that records that it’s been called."""
    class Recorder(object):
        called = False

    def fake_init_db():
        Recorder.called = True

    monkeypatch.setattr('flaskr.db.init_db', fake_init_db)
    result = runner.invoke(args=['init-db'])
    assert 'Initialized' in result.output
    assert Recorder.called