class SchemaErrors(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)
        self.message = message
        self.error_type = "Unprocessable Entity"
        self.status_code = 422

    def error_json(self):
        return  {"message": self.message, "error": str(self.error_type), "status_code": self.status_code}
        
class HttpErrors(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)
        self.message = message
        self.error_type = "Ocorreu um erro inexperado"
        self.status_code = 500

    def error_json(self):
        return  {"message": self.message, "error": str(self.error_type), "status_code": self.status_code}
