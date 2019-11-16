class BaseException(Exception):
    def __init__(self, thrower, reason):
        super().__init__()
        self.__exception_thrower = type(thrower).__name__
        self.__reason = reason

    def __str__(self):
        return "[{}] : {}".format(self.__exception_thrower, self.__reason)


class OptionException(BaseException):
    pass


class DisplayFrameException(BaseException):
    pass


class InputStrategiesException(BaseException):
    pass
