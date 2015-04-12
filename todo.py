from flask import Flask
import flask.ext.sqlalchemy
import flask.ext.restless


app = Flask(__name__,instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')


# Create the Flask-SQLAlchemy object and an SQLite database
# app.config['SQLALCHEMY_DATABASE_URI'] loads from the config file
db = flask.ext.sqlalchemy.SQLAlchemy(app)


class Todo(db.Model):
    """database model"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, unique=False)
    is_completed = db.Column(db.Boolean)

    # When we create a new Todo it should be incomplete and have a title
    def __init__(self, title, is_completed=False):
        self.title = title
        self.is_completed = is_completed


# Create the database tables.
db.create_all()


# Create the Flask-Restless API manager.
restless_manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)


def ember_formatter(result, search_params):
    a = {'todos': result['objects']} if 'page' in result else result
    app.logger.debug(str(a) + str(search_params))
    return {'todos': result['objects']} if 'page' in result else result


def pre_ember_formatter(results):
    app.logger.debug(result)
    app.logger.debug(result['todo'])
    return result['todo']


def pre_patch_ember_formatter(instid, result):
    return result['todo']


# Create API endpoint, which will be available at /api/todos
# restless_manager.create_api(
#     Todo,
#     methods=['GET', 'POST', 'DELETE', 'PUT', 'PATCH'],
#     url_prefix='/api',
#     collection_name='todos',
#     results_per_page=-1,
#     # postprocessors={
#     #     'GET_MANY': [ember_formatter]
#     # },
#     preprocessors={
#         'POST': [pre_ember_formatter],
#         'PUT_SINGLE': [pre_patch_ember_formatter]
#     }
# )


# Create API endpoints, which will be available at /api/<tablename> by
# default. Allowed HTTP methods can be specified as well.
restless_manager.create_api(Todo, methods=['GET', 'POST', 'DELETE'])


# post request example
# r = requests.post('http://localhost/api/person', data=json.dumps(tasks),headers={'content-type': 'application/json'})

# @app.route('/')
# def hello_world():
#     return render_template('index.html')


if __name__ == '__main__':
    app.run()
