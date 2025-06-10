import os

from flask import Flask

from src.app.enterprise.infra.config.banner import show_banner
from src.app.enterprise.infra.config.controller_register import ControllerRegister
from src.app.enterprise.infra.config.middleware_register import MiddlewareRegister


class App:
    def __init__(self):
        self.flask = Flask(__name__)
        self.middleware_handler = MiddlewareRegister(self.flask)
        self.controller_handler = ControllerRegister(self.flask)
        self.is_configured = False

    def __configure(self):
        self.middleware_handler.register()
        self.controller_handler.register()

    def run(self, port=int(os.environ.get("AI_SERVICE_PORT", 5000))):
        self.__configure()
        show_banner()
        self.flask.run(debug=True, host='0.0.0.0', port=port)