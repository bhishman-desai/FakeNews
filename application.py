from flask import *
from main import *

application = Flask(__name__)


@application.route('/', methods=['GET', 'POST'])
def basic():
    return "<h1>Welcome! This is homepage</h1>"


@application.route('/uploads', methods=['GET', 'POST'])
def uploads():
    if request.method == 'POST':
        return redirect(url_for('basic'))
    if True:
        print("TODO")


if __name__ == '__main__':
    application.run(debug=True)
