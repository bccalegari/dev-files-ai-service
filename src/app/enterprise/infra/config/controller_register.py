from flask import Flask

from src.app.enterprise.infra.adapter.container.add_document_app_container import AddDocumentAppContainer
from src.app.enterprise.infra.adapter.container.query_document_app_container import QueryDocumentAppContainer
from src.app.enterprise.infra.adapter.controller.add_document_controller import AddDocumentController
from src.app.enterprise.infra.adapter.controller.query_document_controller import QueryDocumentController
from src.app.enterprise.infra.config.logger import Logger

log = Logger()

class ControllerRegister:
    def __init__(self, flask_app: Flask):
        self.flask_app = flask_app
        self.controllers = [
            AddDocumentController(AddDocumentAppContainer().get_usecase()),
            QueryDocumentController(QueryDocumentAppContainer().get_usecase())
        ]

    def register(self):
        log.info(f"Registering {len(self.controllers)} controller(s)")

        for controller in self.controllers:
            log.info(f"Registering {controller.__class__.__name__}")
            controller.register_routes(self.flask_app)