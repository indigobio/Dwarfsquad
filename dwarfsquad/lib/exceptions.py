class AuthorizationError(BaseException):

    def __init__(self, message):
        self.message = "Login credentials for " + str(message) + " are not valid"
