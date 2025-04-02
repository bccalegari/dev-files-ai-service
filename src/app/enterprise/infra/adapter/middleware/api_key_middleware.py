import os

from flask import request, jsonify

from src.app.enterprise.domain.error_code import ErrorCode
from src.app.enterprise.infra.adapter.dto.response_dto import ResponseDto
from src.app.enterprise.infra.config.logger import Logger

log = Logger()


class ApiKeyMiddleware:
    @staticmethod
    def before_request():
        api_key_mock = os.getenv("API_KEY")
        api_key_from_header = request.headers.get("X-API-KEY")

        if api_key_from_header is None:
            log.error("API key is missing")
            response = ResponseDto.error(ErrorCode.UNAUTHORIZED, "API key is missing")
            return jsonify(response.to_dict()), ErrorCode.UNAUTHORIZED.value.status

        if api_key_from_header != api_key_mock:
            log.error("API key is invalid")
            response = ResponseDto.error(ErrorCode.UNAUTHORIZED, "API key is invalid")
            return jsonify(response.to_dict()), ErrorCode.UNAUTHORIZED.value.status