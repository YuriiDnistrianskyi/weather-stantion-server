class ConflictException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class NotFoundException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class UserIsExistException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class ForbiddenAccessException(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message
