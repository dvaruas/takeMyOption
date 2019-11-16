from .exceptions import InputStrategiesException


class InputStrategies:
    def __init__(self, prompt):
        self.__prompt = prompt

    def inputRawString(self, defaultInput=None):
        __prompt = "{prompt}{default} : ".format(
            prompt=self.__prompt if self.__prompt else "Enter",
            default="[{}]".format(defaultInput) if defaultInput != None else ""
        )
        __i = None
        while True:
            try:
                __i = input(__prompt)
                if len(__i) == 0 and defaultInput:
                    __i = defaultInput
            except (KeyboardInterrupt, EOFError):
                print("\n")
        return __i

    def inputAnOption(self, options, showOptions=False, defaultInput=None):
        if not isinstance(options, list):
            raise InputStrategiesException(self, "options argument must be a list")
        if not isinstance(showOptions, bool):
            raise InputStrategiesException(self, "showOptions argument must be a boolean")
        if defaultInput != None and defaultInput not in options:
            raise InputStrategiesException(self, "The defaultInput argument "
                "should also be in the options argument")

        while True:
            __new_prompt = "{prompt}{opts}{default} : ".format(
                prompt=self.__prompt if self.__prompt else "Enter Choice",
                opts="({})".format("/".join(options)) if showOptions else "",
                default="[{}]".format(defaultInput) if defaultInput != None else ""
            )
            try:
                __i = input(__new_prompt)
            except (KeyboardInterrupt, EOFError):
                print("\n")
                continue
            if len(__i) == 0 and defaultInput:
                return defaultInput
            elif __i in options:
                return __i

    def __str__(self):
        return "InputStrategy for prompt : {}".format(self.__prompt)
