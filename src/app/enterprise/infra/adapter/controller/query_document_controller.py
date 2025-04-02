from flask import Blueprint, request, jsonify, Flask
from pydantic import ValidationError

from src.app.core.application.usecase.query_document_usecase import QueryDocumentUseCase
from src.app.enterprise.domain.error_code import ErrorCode
from src.app.enterprise.infra.adapter.dto.query_document_request_dto import QueryDocumentRequestDto
from src.app.enterprise.infra.adapter.dto.response_dto import ResponseDto
from src.app.enterprise.infra.config.logger import Logger

log = Logger()

class QueryDocumentController:
    def __init__(self, query_document_use_case: QueryDocumentUseCase):
        self.query_document_use_case = query_document_use_case
        self.blueprint = Blueprint("query_document", __name__)
        self._register_routes()

    def _register_routes(self):
        self.blueprint.add_url_rule("/query", "query_document", self.handle_query, methods=["POST"])

    def handle_query(self):
        try:
            data = request.get_json()
            if not data:
                return jsonify(
                    ResponseDto.error(ErrorCode.BAD_REQUEST, "Invalid JSON or empty request").to_dict()
                ), 400

            try:
                request_dto = QueryDocumentRequestDto(**data)
            except ValidationError as e:
                return jsonify(ResponseDto.error(ErrorCode.UNPROCESSABLE_ENTITY, str(e)).to_dict()), 422

            log.info(
                f"Processing query: {request_dto.query} "
                f"| User: {request_dto.user_slug} "
                f"| Document: {request_dto.document_slug}"
            )

            response = self.query_document_use_case.execute(
                request_dto.user_slug, request_dto.document_slug, request_dto.query
            )

            return jsonify(response.to_dict()), 200

        except ValueError as ve:
            return jsonify(ResponseDto.error(ErrorCode.BAD_REQUEST, str(ve)).to_dict()), 400

        except Exception as e:
            log.error(f"Internal Server Error: {str(e)}")
            return jsonify(ResponseDto.error(ErrorCode.INTERNAL_SERVER_ERROR, "Internal Server Error").to_dict()), 500

    def register_routes(self, app: Flask):
        app.register_blueprint(self.blueprint, url_prefix="/api/v1")