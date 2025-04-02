from flask import g, request

from src.app.enterprise.infra.config.logger import Logger
from src.app.enterprise.domain.trace_id import TraceId

log = Logger()


class TraceIdMiddleware:
    @staticmethod
    def before_request():
        trace_id_from_header = request.headers.get('X-Trace-ID')

        trace_id = TraceId(trace_id_from_header).value
        g.trace_id = trace_id
        log.bind(trace_id=trace_id)

        if trace_id_from_header:
            log.info(f"Request for route: {request.path} with trace id: {trace_id_from_header}")
        else:
            log.info(f"Request for route: {request.path} without trace id, generating a new one")

        log.info(f"Trace id added to context: {trace_id}")

    @staticmethod
    def after_request(response):
        log.info(f"Response for route: {request.path} with trace id: {g.trace_id}")
        log.info("Cleaning up the context")

        del g.trace_id
        log.unbind("trace_id")

        return response