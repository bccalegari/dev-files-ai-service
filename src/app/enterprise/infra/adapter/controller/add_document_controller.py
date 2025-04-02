from flask import Blueprint, request, jsonify, Flask
from pydantic import ValidationError

from src.app.core.application.usecase.add_document_usecase import AddDocumentUseCase
from src.app.enterprise.domain.error_code import ErrorCode
from src.app.enterprise.infra.adapter.dto.add_document_request_dto import AddDocumentRequestDto
from src.app.enterprise.infra.adapter.dto.response_dto import ResponseDto
from src.app.enterprise.infra.config.logger import Logger

log = Logger()

class AddDocumentController:
    def __init__(self, add_document_use_case: AddDocumentUseCase):
        self.add_document_use_case = add_document_use_case
        self.blueprint = Blueprint("add_document", __name__)
        self._register_routes()

    def _register_routes(self):
        self.blueprint.add_url_rule("/embedding", "add_document", self.handle_insert, methods=["POST"])

    def handle_insert(self):
        try:
            data = request.get_json()
            if not data:
                return jsonify(
                    ResponseDto.error(ErrorCode.BAD_REQUEST, "Invalid JSON or empty request").to_dict()
                ), 400

            try:
                request_dto = AddDocumentRequestDto(**data)
            except ValidationError as e:
                return jsonify(ResponseDto.error(ErrorCode.UNPROCESSABLE_ENTITY, str(e)).to_dict()), 422

            log.info(
                f"Processing document with url: {request_dto.url} "
                f"| User: {request_dto.user_slug} "
                f"| Document: {request_dto.document_slug}"
            )

            response = self.add_document_use_case.execute(
                request_dto.url, request_dto.user_slug, request_dto.document_slug
            )

            return jsonify(response.to_dict()), 200

        except ValueError as ve:
            return jsonify(ResponseDto.error(ErrorCode.BAD_REQUEST, str(ve)).to_dict()), 400

        except Exception as e:
            log.error(f"Internal Server Error: {str(e)}")
            return jsonify(ResponseDto.error(ErrorCode.INTERNAL_SERVER_ERROR, "Internal Server Error").to_dict()), 500

    def register_routes(self, app: Flask):
        app.register_blueprint(self.blueprint, url_prefix="/api/v1")