from datetime import datetime

from src.app.enterprise.domain.error_code import ErrorCode


class ResponseDto:
    def __init__(self, metadata: dict, data: dict = None, error: dict = None):
        self.metadata = self.Metadata(metadata)
        if data:
            self.data = self.Data(data)
        if error:
            self.error = self.Error(error)

    def to_dict(self):
        response = {
            "metadata": self.metadata.to_dict()
        }
        if hasattr(self, "data"):
            response["data"] = self.data.to_dict()
        elif hasattr(self, "error"):
            response["error"] = self.error.to_dict()
        return response

    class Metadata:
        def __init__(self, metadata: dict):
            self.message = metadata["message"]
            self.timestamp = metadata["timestamp"]

        def to_dict(self):
            return {
                "message": self.message,
                "timestamp": self.timestamp
            }

    class Data:
        def __init__(self, data: dict):
            self.data = data

        def to_dict(self):
            return self.data

    class Error:
        def __init__(self, error: dict):
            self.code = error["code"]
            self.message = error["message"]

        def to_dict(self):
            return {
                "code": self.code,
                "message": self.message
            }

    @classmethod
    def success(cls, data: dict):
        return cls(
            metadata={
                "message": "Request was successful",
                "timestamp": datetime.now().isoformat()
            },
            data=data
        )

    @classmethod
    def error(cls, error_code: ErrorCode, message: str):
        return cls(
            metadata={
                "message": "Something went wrong, please try again later",
                "timestamp": datetime.now().isoformat()
            },
            error={
                "code": error_code.value.code,
                "message": message
            }
        )