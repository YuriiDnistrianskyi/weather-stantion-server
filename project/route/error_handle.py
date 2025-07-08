from http import HTTPStatus
from flask import Blueprint, Response, make_response

error_handle_bp = Blueprint("error", __name__)

@error_handle_bp.app_errorhandler(HTTPStatus.NOT_FOUND)
def not_found(error: int) -> Response:
    return make_response("Object not found", HTTPStatus.NOT_FOUND)

@error_handle_bp.app_errorhandler(HTTPStatus.UNPROCESSABLE_ENTITY)
def unprocessable_entity(error: int) -> Response:
    return make_response("Input data is wrong or not full", HTTPStatus.UNPROCESSABLE_ENTITY)

@error_handle_bp.app_errorhandler(HTTPStatus.CONFLICT)
def conflict(error: int) -> Response:
    return make_response("Conflict data", HTTPStatus.CONFLICT)

@error_handle_bp.app_errorhandler(HTTPStatus.METHOD_NOT_ALLOWED)
def method_not_allowed(error: int) -> Response:
    return make_response("Method not allowed", HTTPStatus.METHOD_NOT_ALLOWED)

# @error_handle_bp.app_errorhandler(HTTPStatus.BAD_REQUEST)
# def bad_request(error: int) -> Response:
#     return make_response("Bad request", HTTPStatus.BAD_REQUEST)
