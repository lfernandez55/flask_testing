# flask_testing

This is a very simple demo of how to use pytest in combination with a flask app.

It uses pytest as well as flask-pytest.

It is based off an example at:  https://github.com/pytest-dev/pytest-flask/issues/7
Also see these docs: https://docs.pytest.org/en/latest/contents.html

To run it:

Clone app
Install and activate venv
pip install -r requirements.txt
flask run (to verify that the server runs)
turn off the server
pytest  (pytest looks for all files with the prefix "test_" and runs them
        it also runs conftest.py which gives test_app some info to test
        the program)
