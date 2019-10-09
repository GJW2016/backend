from flask import render_template
from flask import Blueprint
from flask import url_for
from flask import Flask, jsonify
from backend.model import Country, Contents, Tags, Events, Festival, Quiz, Recipe, Restaurant

main = Blueprint('main', __name__, template_folder='templates', static_folder='static', static_url_path="/static")


@main.route('/countries')
def get_countries():
    country = Country.query.all()
    return jsonify(json_list=[i.serialize for i in country])


@main.route('/tags')
def get_tags():
    tags = Tags.query.all()
    return jsonify(json_list=[i.serialize for i in tags])


@main.route('/contents')
def get_contents():
    contents = Contents.query.all()
    return jsonify(json_list=[i.serialize for i in contents])


@main.route('/events')
def get_events():
    events = Events.query.all()
    return jsonify(json_list=[i.serialize for i in events])


@main.route('/festivals')
def get_festivals():
    festivals = Festival.query.all()
    return jsonify(json_list=[i.serialize for i in festivals])


@main.route('/quizzes')
def get_quizzes():
    quizzes = Quiz.query.all()
    return jsonify(json_list=[i.serialize for i in quizzes])


@main.route('/recipes')
def get_recipes():
    recipes = Recipe.query.all()
    return jsonify(json_list=[i.serialize for i in recipes])


@main.route('/restaurants')
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify(json_list=[i.serialize for i in restaurants])


@main.route('/', defaults={'path': ''})
@main.route('/<path:path>')
def index(path):
    return render_template('index.html')
