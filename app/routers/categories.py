from flask import Blueprint, request, jsonify, abort
from pydantic import ValidationError

from app.models import db, Category

from app.schemas.questions import CategoryRead, CategoryBase

from app.contracts import *


categories_bp = Blueprint('categories', __name__)


@categories_bp.route('/', methods=['GET', 'POST'])
def categories():
    if request.method == "GET":
        items = Category.query.all()
        result = [CategoryRead.model_validate(item).model_dump() for item in items]
        return jsonify(result), 200
    if request.method == "POST":
        try:
            raw = request.get_json(silent=False)
        except Exception as e:
            return jsonify(ErrorResponse(error="JSON is not valid").model_dump()), 400

        if not raw:
            return jsonify(ErrorResponse(error="No data").model_dump()), 400

        try:
            data = CategoryBase.model_validate(raw)
            category = Category(**data.model_dump())
            db.session.add(category)
            db.session.commit()

            return jsonify(CategoryRead.model_validate(category).model_dump()), 201

        except ValidationError as e:
            return jsonify(ErrorResponse(error="Data is not valid").model_dump()), 400

@categories_bp.route('/<int:id>', methods=['PUT', 'DELETE'])
def category(id):
    category = db.session.get(Category, id)
    if not category:
        return jsonify(ErrorResponse(error=f"Category not found with id={id}").model_dump()), 404

    if request.method == "PUT":
        try:
            raw = request.get_json(silent=False)
        except Exception as e:
            return jsonify(ErrorResponse(error="JSON is not valid").model_dump()), 400

        if not raw:
            return jsonify(ErrorResponse(error="No data").model_dump()), 400

        try:
            data = CategoryBase.model_validate(raw)
            category.name = data.name
            db.session.commit()

            return jsonify(CategoryRead.model_validate(category).model_dump()), 200
        except ValidationError as e:
            return jsonify(ErrorResponse(error="Data is not valid").model_dump()), 400

    if request.method == "DELETE":
        # try
        db.session.delete(category)
        db.session.commit()
        return '', 204