class BaseException(Exception):
    def __init__(self, thrower, reason):
        super().__init__()
        self.__exception_thrower = type(thrower).__name__
        self.__reason = reason

    def __str__(self):
        return "[{}] : {}".format(self.__exception_thrower, self.__reason)


class OptionException(BaseException):
    """Exception raised when there is any problem with setting of options."""
    pass


class DisplayFrameException(BaseException):
    """Exception raised when there is any problem while building Display Frame."""
    pass


class InputStrategiesException(BaseException):
    """Exception raised when there is any problem regarding taking input from user."""
    pass
