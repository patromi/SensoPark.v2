import os
import logging
from app import create_app, db, count
#from app.models import User, Role
from flask_migrate import Migrate

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)
@app.shell_context_processor
def make_shell_context():
    return dict(db=db)

@app.cli.command()
def test():
    """Uruchom testy jednostkowe. Narazie nie działa pieprzy sie cos z bazą danych
    tzn. wszystko sie usuwa xD"""
    import unittest
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=2).run(tests)


import asyncio
if __name__ == '__main__':
    app.run(debug=True)
    logging.getLogger().setLevel("DEBUG")
