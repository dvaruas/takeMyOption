from .exceptions import InputStrategiesException


class InputStrategies:
    def __init__(self, prompt=""):
        """Constructor for InputStrategies

        Args:
            prompt(:obj:`str`, optional): The prompt to display while taking input.

        Raises:
            :obj:`~takeMyOption.exceptions.InputStrategiesException`: Raised if
                prompt is not a String.
        """
        if not isinstance(prompt, str):
            raise InputStrategiesException(self, "prompt argument should be a string."
                " Invalid value : {}(type : {})")
        self.__prompt = prompt

    def inputRawString(self, defaultInput=None):
        """Take a Raw String as input from the user.

        Args:
            defaultInput(any, optional): If user enters a blank string, take this value.

        Returns:
            String entered by the user or defaultInput if provided.
        """
        __prompt = "{prompt}{default} : ".format(
            prompt=self.__prompt if self.__prompt else "Enter",
            default=" [{}]".format(defaultInput) if defaultInput != None else ""
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
        """Takes choice from a list of options given to user.

        Args:
            options(:obj:`list`): A list of the choices which are valid inputs.
            showOptions(:obj:`bool`, optional): show the user the options with the prompt. Eg - (1/2/3).
            defaultInput(any, optional): If user enters a blank string, take this value.

        Returns:
            Option entered by the user or defaultInput if provided.

        Raises:
            :obj:`~takeMyOption.exceptions.InputStrategiesException`: If options
                is not a list. If showOptions is not a boolean.
                If defaultInput is not in the options list.
        """
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
                opts=" ({})".format("/".join(options)) if showOptions else "",
                default=" [{}]".format(defaultInput) if defaultInput != None else ""
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
