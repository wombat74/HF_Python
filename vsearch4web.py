from curses.ascii import US
from flask import Flask, render_template, request, escape, session
from mysqlx import InterfaceError
from DBcm import SQLError, UseDatabase, ConnectionError, CredentialsError
from checker import check_logged_in

app = Flask(__name__)

app.secret_key = ';fksdjhgkhewotugqwgeiouhbdbvnk'

app.config['dbconfig'] = { 'host': '127.0.0.1',
                           'user': 'vsearch',
                           'password': 'vsearchpasswd',
                           'database': 'vsearchlogDB', }

def search4letters(phrase:str, letters:str='aeiou') -> set:
    """Return a set of 'letters' found in 'phrase'"""
    return set(letters).intersection(set(phrase))

@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in.'

@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'You are now logged out.'


def log_request(req: 'flask_request', res: str) -> None:
    """Configure connection to database, write values to log table"""

    with UseDatabase(app.config['dbconfig']) as cursor:

        _SQL = """INSERT INTO log (phrase, letters, ip, browser_string, results)
                VALUES (%s, %s, %s, %s, %s)"""

        cursor.execute(_SQL, (req.form['phrase'],
                              req.form['letters'],
                              req.remote_addr,
                              req.user_agent.browser,
                              res, ))


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    """Extract the posted data; perform the search; return results."""

    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))

    try:
        log_request(request, results)
    except ConnectionError as err:
        print('There has been a connection error, please check database!:', str(err))
    except Exception as err:
        print('****There has been an exception:', str(err))

    return render_template('results.html',
                            the_title=title,
                            the_phrase=phrase,
                            the_letters=letters,
                            the_results=results,)

@app.route('/viewlog')
@check_logged_in
def view_the_log() -> 'html':
    """Display the contents of the log file as an HTML table."""
    try:
        with UseDatabase(app.config['dbconfig']) as cursor:

            _SQL = """SELECT phrase, letters, ip, browser_string, results FROM log"""

            cursor.execute(_SQL)
            contents = cursor.fetchall()

        titles = ('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results')

        return render_template('viewlog.html',
                                the_title='View Log',
                                the_row_titles=titles,
                                the_data=contents,)

    except ConnectionError as err:
        print('Is your database turned on? Error:', str(err))
    except CredentialsError as err:
        print('User-id/Password issues. Error:', str(err))
    except SQLError as err:
        print('Is your query correct? Error:', str(err))
    except Exception as err:
        print('There has been an exception:', str(err))
    return 'Error'


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                            the_title='Welcome to search4letters on the web!')


if __name__ == '__main__':
    app.run(debug=True)