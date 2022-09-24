
from app import create_app


__author__ = 'July'

app = create_app()
#print(app.config['DEBUG']) # need capitial letter

from app.web import book

if __name__ == '__main__':
    print('active: ' + str(id(app)))
    # prod using nginx + uwsgi
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=8080)

