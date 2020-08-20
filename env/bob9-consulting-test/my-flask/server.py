from flask import Flask
from flask_graphql import GraphQLView
import schema

app = Flask(__name__)

@app.route('/')
def default_route():
	return "Hello, Default Route!"

@app.route('/index')
def index():
	return "Hello, World!"

@app.route('/get_name')
def get_name():
	return "My name flask!"

@app.route('/get_app_version')
def get_app_name():
	return "0.0.7"

app.add_url_rule(
  '/gql',
  view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)

app.run()

