from src.app.enterprise.infra.adapter.middleware.api_key_middleware import ApiKeyMiddleware
from src.app.enterprise.infra.adapter.middleware.trace_id_middleware import TraceIdMiddleware
from src.app.enterprise.infra.config.logger import Logger

log = Logger()

class MiddlewareRegister:
    def __init__(self, app):
        self.app = app
        self.middlewares = [
            TraceIdMiddleware, ApiKeyMiddleware
        ]

    def register(self):
        log.info(f"Registering {len(self.middlewares)} middleware(s)")

        for middleware in self.middlewares:
            log.info(f"Registering {middleware.__name__}")
            if hasattr(middleware, "before_request"):
                self.app.before_request(middleware.before_request)
            if hasattr(middleware, "after_request"):
                self.app.after_request(middleware.after_request)

        log.info(f"Registered {len(self.middlewares)} middleware(s)")