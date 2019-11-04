"""This module contains the two main cli commands: run and test."""

import os
import unittest

from flask_script import Manager

from app.main import create_app

# Note: why is this being imported? It's not being used...
# from app.main.model import campaign
from app import blueprint

app = create_app(os.getenv('ENV') or 'dev')

app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def run():
    """This function runs the app"""
    app.run()


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()
