import os
from flask import Flask
from app import create_app
from app.models import Question, db
import pytest

os.environ['FLASK_ENV'] = 'testing'
# app = Flask(__name__)
# @app.route('/')
# def index():


def make_client():
    app = create_app()
    with app.app_context():
        db.create_all()
    return app.test_client(), app


def test_create_questin():
    client, app = make_client()
    resp = client.post('/questions/', json={'text': 'How are you today?'})

    assert resp.status_code == 201
    data = resp.get_json()
    assert data['text'] == 'How are you today?'
    assert 'id' in data


def test_create_questin_with_spaces():
    client, app = make_client()
    resp = client.post('/questions/', json={'text': '           How are you today?         '})

    assert resp.status_code == 201
    data = resp.get_json()
    assert data['text'] == 'How are you today?'
    assert 'id' in data



def test_list_questions():
    client, app = make_client()
    resp = client.get('/questions/')
    assert resp.status_code == 200
    data = resp.get_json()
    # assert data['count'] > 0