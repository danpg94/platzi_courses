This project requires specifically Python 3.8 to function correctly

To create a virtual enviornment:

1. pip install virtualenv 

2. (Windows) py -3.8-64 -m venv venv
2. (Linux)   python3.8 -m venv venv

3. (Windows) venv\Scripts\activate
3. (Linux)   source venv/bin/activate

4. pip install -r requirements.txt

To run REPL:
python main.py

To run tests:
Windows:
    Check for errors in code: mypy .
    Run unit tests:           nosetests

Linux:
    Run both:               : mypy . && nosetests