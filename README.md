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
        --https://docs.pytest.org/en/latest/goodpractices.html#test-discovery--

        it also runs conftest.py which gives test_app some info to test
        the program

        if you only want to run one of the test files you can call it by name
        example:  pytest -q test_app.py
