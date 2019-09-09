from flask import render_template
from flask import Blueprint
from flask import url_for
from flask import Flask, jsonify
from backend.model import Country, Contents, Tags

main = Blueprint('main', __name__, template_folder='templates', static_folder='static', static_url_path="/static")


@main.route('/countries')
def get_countries():
    country = Country.query.all()
    return jsonify(json_list=[i.serialize for i in country])
    #return jsonify(json_list=[i.serialize for i in country.country_content])


@main.route('/tags')
def get_tags():
    tags = Tags.query.all()
    return jsonify(json_list=[i.serialize for i in tags])


@main.route('/contents')
def get_contents():
    contents = Contents.query.all()
    return jsonify(json_list=[i.serialize for i in contents])


@main.route('/', defaults={'path': ''})
@main.route('/<path:path>')
def index(path):
    return render_template('index.html')
